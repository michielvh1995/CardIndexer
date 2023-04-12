import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs';


import { Card } from './card';
import { getCardOverview, CARDS } from './card-list';
import { MessageService } from './message.service';

import { HttpClient, HttpHeaders } from '@angular/common/http';



interface CardResponse {
  cards : Card[];
}

@Injectable({
  providedIn: 'root'
})
export class CardService {

  private cardURL = 'https://api.magicthegathering.io/v1/cards';

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

  

  // We are currently ignoring the cards data base of the cards I own.
  // This will be fixed once I implement MongoDB
  getCards() : Observable<Card[]> {
    // See https://angular.io/tutorial/tour-of-heroes/toh-pt4 to get it to do HTTP Requests
    const cards = of(getCardOverview());
    this.log('fetched cards');
    return cards;
  }


  // When getting the detailed information of the card in question we call the official gatherer API
  getCard(internal_id: number): Observable<Card> {
    // For now, assume that a hero with the specified `id` always exists.
    // Error handling will be added in the next step of the tutorial.
    const card = getCardOverview().find(h => h.internal_id === internal_id)!;
    
    return of(card);

    this.log(`fetching card name=${card.name} from external`);

    return this.http.get<CardResponse>(`${this.cardURL}?name="${card.name}"`)
      .pipe(
        map(cards => {console.log(cards); return cards["cards"][0]}), // returns a {0|1} element array
        tap(h => {
          const outcome = h ? 'fetched' : 'did not find';
          this.log(`${outcome} card id=${internal_id}`);

        }),
        catchError(this.handleError<Card>(`getCard id=${internal_id}`))
      ); 
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  private log(message: string) {
    this.messageService.add(`CardService: ${message}`);
  }
}
