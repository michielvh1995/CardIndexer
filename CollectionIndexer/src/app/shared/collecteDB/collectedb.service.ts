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

    private apiURL = "http://localhost:8000/"

    getAllCards(): Observable<Card[]> {
      return this.http.get<APICards>(`${this.apiURL}cards/all`)
        .pipe(
          catchError(this.handleError<APICards>('Get all cards', {"Cards":[]})),
          map(fetched => fetched.Cards),
          tap(fetched => this.log(`Fetched ${fetched.length} cards`))
        );
    }

    getCardbyInternalID(internalID : number): Observable<Card>{
      return this.http.get<APICards>(`${this.apiURL}cards?internal_id=${internalID}`)
        .pipe(
          tap(fetched => this.log(`${fetched.Cards}`)),
          catchError(this.handleError<APICards>('Get cards by internal ID', {"Cards":[]})),
          map(fetched => fetched.Cards[0]),
          tap(fetched => this.log(`Fetched ${fetched.name}`))
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
