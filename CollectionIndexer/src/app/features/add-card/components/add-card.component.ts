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
  ) {
    
  }

  items? : APICard[];
  submittedStatus = [true];

  addCards(cards : APICard[]) {
    this.items = cards;
    
    // This is done to create a new instance of the mutli-card-selector
    this.collecteDBService.postNewCards(cards).subscribe(result => {
      if (!result) {
        this.submittedStatus[this.submittedStatus.length-1] = false;
        console.log("failed");
      }
      else {
        this.submittedStatus[this.submittedStatus.length-1] = true;
        this.submittedStatus[this.submittedStatus.length] = false;
        
        console.log('success');
      }
      console.log(this.submittedStatus);
    });

  }

  goBack(): void {
    this.location.back();
  }
}
