import { Component, OnInit } from '@angular/core';
import { Card } from '../shared/models/card';
import { CardService } from '../features/card/services/card.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: [ './dashboard.component.css' ]
})
export class DashboardComponent implements OnInit {
  cards: Card[] = [];

  constructor(private cardService: CardService) { }

  ngOnInit(): void {
    this.getcards();
  }

  getcards(): void {
    this.cardService.getCards()
      .subscribe(cards => this.cards = cards.slice(1, 5));
  }
}