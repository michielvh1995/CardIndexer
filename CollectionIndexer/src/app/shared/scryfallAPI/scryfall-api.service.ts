import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MessageService } from '../messages/services/message.service';

@Injectable({
  providedIn: 'root'
})
export class ScryfallAPIService {

  constructor(
    private http : HttpClient,
    private messageService : MessageService
    ) { }


}


interface ScryfallCardAPIModel {
  object : string;

  // Error response:
  code? : string;
  status? : number;
  details? : string;

  // Success response:
  id? : string;
  multiverse_ids? : number[];
  cardmarket_id? : number;
  image_uris? : { [key:string] : string };
  promo_types? : string[];
}