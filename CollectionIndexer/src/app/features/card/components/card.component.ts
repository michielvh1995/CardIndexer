import { Component } from '@angular/core';

import { Card } from '../../../shared/models/card'; 
import { CardService } from '../services/card.service';
import { MessageService } from '../../../shared/messages/services/message.service';
import { CollectedbService } from 'src/app/shared/collecteDB/collectedb.service';


@Component({
  selector: 'app-card',
  templateUrl: '../pages/card.component.html',
  styleUrls: ['../pages/card.component.css']
})

export class CardComponent {
  cards: Card[] = [];

  constructor(private cardService: CollectedbService, private messageService: MessageService) {}

  ngOnInit(): void {
    this.getAllCards();
  }

  getAllCards() : void {
    this.cardService.getAllCards().subscribe(fetched => this.cards = fetched);
  
  }
}
