import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { MessageService } from '../messages/services/message.service';
import { Observable, catchError, map, of, tap } from 'rxjs';
import { Card } from '../models/card';
import { CardsAPIModel, APICard, CardVersion } from '../models/api';

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


    packAPICard(card : Card) : APICard {
      let version : CardVersion = {
        "card_count": card.card_count,
        "multiverseID" : card.multiverseID,
        "set_code" : card.set_code,
        "foil" : card.foil
      };
      
      this.log(`version cc: ${version.card_count}`);

      return {
        "internal_id" : card.internal_id,
        "name" : card.name,
        "versions" : [version]
      };
    }

    unpackAPICard(card : APICard) : Card[] {
      var unpacked = []
      for (let index = 0; index < card.versions.length; index++) {
        const version = card.versions[index];
        unpacked.push({
          "internal_id" : card.internal_id,
          "name": card.name,
          "card_count": version.card_count,
          "multiverseID" : version.multiverseID,
          "set_code" : version.set_code,
          "foil" : version.foil
        });
      }
      return unpacked as Card[];
    }

    unpackCardAPIModel(cards : CardsAPIModel) : Card[] {
      var cardsArray : Card[] = [];
      for (let index = 0; index < cards.Cards.length; index++) {
        cardsArray = cardsArray.concat(this.unpackAPICard(cards.Cards[index]));
      }
      return cardsArray;
    }


    getAllCards(): Observable<Card[]> { 
      return this.http.get<CardsAPIModel>(`${this.apiURL}cards/all`)
        .pipe(
          catchError(this.handleError<CardsAPIModel>('Get all cards', {"Cards":[]})),
          map(fetched => this.unpackCardAPIModel(fetched)),
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
      return this.http.get<CardsAPIModel>(`${this.apiURL}cards${queryString}`)
        .pipe(
          catchError(this.handleError<CardsAPIModel>('Get cards by internal ID', {"Cards":[]})),
          map(fetched => fetched.Cards),  // Extract the fetched cards
          tap(fetched => this.log(`Fetched ${fetched.length} cards`)) // Log success
        );
    }

    // 
    searchCardsByField(field:string, value:string) {
      return this.http.get<CardsAPIModel>(`${this.apiURL}cards?${field}=${value}`)
        .pipe(
          catchError(this.handleError<CardsAPIModel>('Get cards by internal ID', {"Cards":[]})),
          map(fetched => fetched.Cards[0]), // Extract the cards from the response
          tap(fetched => this.log(`Fetched ${fetched.name}`))
        );
    }

    // I do not like this function as the card name is the primary UID
    getCardbyInternalID(internalID : number): Observable<Card>{
      return this.http.get<CardsAPIModel>(`${this.apiURL}cards?internal_id=${internalID}`)
        .pipe(
          catchError(this.handleError<CardsAPIModel>('Get cards by internal ID', {"Cards":[]})),
          map(fetched => this.unpackCardAPIModel(fetched)[0]), // Extract the cards from the response
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

    // Currently I use a jank-ass packing function to wrap cards into the new APi format
    // The rest of the program will have to be rewritten to use the better format
    postNewCard(card : Card) : Observable<Card> {
      this.log(`Card to be posted: ${card.card_count}`)
      let cardWrapper : CardsAPIModel = {"Cards" : [this.packAPICard(card)]};

      return this.http.post<CardsAPIModel>(`${this.apiURL}cards/new/`, cardWrapper, this.httpOptions).pipe(
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
