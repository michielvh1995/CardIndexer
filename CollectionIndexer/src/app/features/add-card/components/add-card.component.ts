import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { CollectedbService } from 'src/app/shared/collecteDB/collectedb.service';
import { Card } from 'src/app/shared/models/card';

@Component({
  selector: 'app-add-card',
  templateUrl: '../pages/add-card.component.html',
  styleUrls: ['../pages/add-card.component.css']
})
export class AddCardComponent {
  constructor(
    private location : Location,
    private collecteDBService : CollectedbService
  ) { }
  
  

  add(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.collecteDBService.postNewCard({ name, "card_count" : 1 } as Card).subscribe(hero => {
      this.goBack();
    });
  }

  goBack(): void {
    this.location.back();
  }
}
