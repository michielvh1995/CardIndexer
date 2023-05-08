import { Component } from '@angular/core';

import { Card } from '../../../shared/models/card'; 
import { CardService } from '../services/card.service';
import { MessageService } from '../../../shared/messages/services/message.service';

@Component({
  selector: 'app-card',
  templateUrl: '../pages/card.component.html',
  styleUrls: ['../pages/card.component.css']
})

export class CardComponent {
  cards: Card[] = [];

  constructor(private cardService: CardService, private messageService: MessageService) {}

  ngOnInit(): void {
    this.getCards();
  }

  getCards() : void {
    this.cardService.getCards().subscribe(cards => this.cards = cards);
  
  }
}
