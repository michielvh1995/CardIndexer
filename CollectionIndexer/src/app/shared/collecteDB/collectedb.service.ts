import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { MessageService } from '../messages/services/message.service';
import { Observable, catchError, map, of, tap } from 'rxjs';
import { Card } from '../models/card';
import { APICards } from '../models/api';

@Injectable({
  providedIn: 'root'
})

export class CollectedbService {
  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

    private log(message: string) {
      this.messageService.add(`CollecteDB API Service: ${message}`);
    }

    // URL for the API, this needs to be configurable from a config file in the future
    private apiURL = "http://localhost:8000/"

    httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };

    getAllCards(): Observable<Card[]> { 
      return this.http.get<APICards>(`${this.apiURL}cards/all`)
        .pipe(
          catchError(this.handleError<APICards>('Get all cards', {"Cards":[]})),
          map(fetched => fetched.Cards),  // Extract the fetched cards
          tap(fetched => this.log(`Fetched ${fetched.length} cards`)) // Log success
        );
    }
  
    searchCardsByFieldsValues(parameters : {[field : string]: string}) {
      
      // First we build up the query string based on the field-value pairs; so it becomes:
      // ?field1=valu1e&field2=value2&
      var queryString = `?`
      for (const key in parameters) {
        if (Object.prototype.hasOwnProperty.call(parameters, key)) {
          queryString += `${key}=${parameters[key]}&`;
        }
      }

      // And then we query the server, with the query string
      return this.http.get<APICards>(`${this.apiURL}cards${queryString}`)
        .pipe(
          catchError(this.handleError<APICards>('Get cards by internal ID', {"Cards":[]})),
          map(fetched => fetched.Cards),  // Extract the fetched cards
          tap(fetched => this.log(`Fetched ${fetched.length} cards`)) // Log success
        );
    }

    searchCardsByField(field:string, value:string) {
      return this.http.get<APICards>(`${this.apiURL}cards?${field}=${value}`)
        .pipe(
          catchError(this.handleError<APICards>('Get cards by internal ID', {"Cards":[]})),
          map(fetched => fetched.Cards[0]), // Extract the cards from the response
          tap(fetched => this.log(`Fetched ${fetched.name}`))
        );
    }

    getCardbyInternalID(internalID : number): Observable<Card>{
      return this.http.get<APICards>(`${this.apiURL}cards?internal_id=${internalID}`)
        .pipe(
          catchError(this.handleError<APICards>('Get cards by internal ID', {"Cards":[]})),
          map(fetched => fetched.Cards[0]), // Extract the cards from the response
          tap(fetched => this.log(`Fetched ${fetched.name}`))
        );
    }

    // I do not like this function as the card name is the primary UID
    updateCardbyID(internalID : number, newValues : Card) : Observable<any> {
      return this.http.put(`${this.apiURL}cards/updatebyID/${internalID}`, newValues, this.httpOptions ).pipe(
        catchError(this.handleError<any>('Update card')),
        tap(response => this.log(`Updated ${internalID} on fields: ${response["updated"]}`))
      );
    }

    postNewCard(card : Card) : Observable<Card> {
      let cardWrapper : APICards = {"Cards" : [card]}
      this.log(`Called postNewCard, with ${cardWrapper.Cards}`)


      return this.http.post<APICards>(`${this.apiURL}cards/new/`, cardWrapper, this.httpOptions).pipe(
        map(newCards => newCards.Cards[0]),
        tap(newCards => this.log(`Added ${newCards.name}`)),
        catchError(this.handleError<any>('PostNewCard'))
      );
    }
    

    private handleError<T>(operation = 'default operation', result?: T){
      return (error: any): Observable<T> => {

        // TODO: send the error to remote logging infrastructure
        console.error(error); // log to console instead
    
        // TODO: better job of transforming error for user consumption
        this.log(`${operation} failed: ${error.message}`);
    
        // Let the app keep running by returning an empty result.
        return of(result as T);
      };
    }
}
