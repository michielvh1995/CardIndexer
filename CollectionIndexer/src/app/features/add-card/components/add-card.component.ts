import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { CollectedbService } from 'src/app/shared/collecteDB/collectedb.service';
import { APICard } from 'src/app/shared/models/api';

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
    
    let cardVers = [{"card_count" : 1}];
    this.collecteDBService.postNewCard({ name, "versions" : cardVers } as APICard).subscribe(hero => {
      this.goBack();
    });
  }

  goBack(): void {
    this.location.back();
  }
}
