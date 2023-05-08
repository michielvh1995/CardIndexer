import { Component, OnInit } from '@angular/core';
import { Card } from '../../../shared/models/card';
import { CardService } from '../../card/services/card.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: '../pages/dashboard.component.html',
  styleUrls: [ '../pages/dashboard.component.css' ]
})
export class DashboardComponent implements OnInit {
  cards: Card[] = [];

  constructor(private cardService: CardService) { }

  ngOnInit(): void {
    this.getcards();
  }

  getcards(): void {
    this.cardService.getCards()
      .subscribe(cards => this.cards = cards.slice(0, 5));
  }
}