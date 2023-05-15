import { Component, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Card } from '../shared/models/card';
import { CollectedbService } from '../shared/collecteDB/collectedb.service';


@Component({
  selector: 'app-card-detail',
  templateUrl: './card-detail.component.html',
  styleUrls: ['./card-detail.component.css']
})
export class CardDetailComponent {
  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private collectedbService: CollectedbService
  ) {}

  ngOnInit(): void {
    this.getCard();
  }

  getCard(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.collectedbService.searchCardsByFieldsValues({})
      .subscribe(card => this.card = card[0]);
    
    // this.collectedbService.getCardbyInternalID(id)
    //   .subscribe(card => this.card = card);
  }

  goBack(): void {
    this.location.back();
  }

  @Input() card? : Card;
}
