import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MessageService } from '../messages/services/message.service';
import { Observable, catchError, of, map, tap } from 'rxjs';
import { Card } from '../models/card';

@Injectable({
  providedIn: 'root'
})

export class WizardsAPIService {

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

    private log(message: string) {
      this.messageService.add(`Wizards API Service: ${message}`);
    }

    // URL for the API, this needs to be configurable from a config file in the future
    private apiURL = "https://api.magicthegathering.io/v1/cards"
    // private apiURL = "https://api.scryfall.com"

    httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };

    castAPIIntoCardObjects(fetchedCards : wizardsAPICardObject) {
      var cardsArray = [];
      for (let i = 0; i < fetchedCards.cards.length; i++) {
        const card = fetchedCards.cards[i];

        console.log(`${card.set}, ${card.number}`); // DEBUG

        cardsArray.push({
          "internal_id" : 1000 + card.number,
          "name": card.name,
          "multiverseID" : card.multiverseid,
          "set_code" : card.set.toLowerCase(),
          "number" : card.number
        })
      }
      return cardsArray as Card[];
    }

    // TODO: Rewrite this function, to be more consistent with what card prototype is being used
    getMultiverseIDByNameAndSet(name? : string, set? : string) {
      var querystring = `?name=${name}&set=${set}`

      this.log(`${this.apiURL}${querystring}`);
      return this.http.get<wizardsAPICardObject>(`${this.apiURL}${querystring}`)
      .pipe(
        catchError(this.handleError("Get multiverseID by name and set", {"cards":[]})),
        tap(fetched => this.log(`${fetched.cards.length} cards from wizards`)),
      )
    }

    queryCardsByNameAndSet(name? : string, set? : string) {
      var querystring = `?name=${name}&set=${set}`

      this.log(`${this.apiURL}${querystring}`);

      return this.http.get<any>(`${this.apiURL}${querystring}`)
        .pipe(
          catchError(this.handleError("Get multiverseID by name and set", [])),
          tap(fetched => this.log(`${fetched.cards.length} cards from wizards`)),
          map(fetched => this.castAPIIntoCardObjects(fetched))
        )
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


interface wizardsAPICardObject {
  cards: [wizardsCardObject];
}

interface wizardsCardObject {
  name : string;
  multiverseid? : number;
  set : string;
  number : number;
}