import { Component } from '@angular/core';

import { Card } from '../card'; 
import { CardService } from '../card.service';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
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
