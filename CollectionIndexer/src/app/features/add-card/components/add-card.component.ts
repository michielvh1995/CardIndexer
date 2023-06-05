import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { CollectedbService } from 'src/app/shared/collecteDB/collectedb.service';
import { APICard, CardVersion } from 'src/app/shared/models/api';

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
  
  multiverseID : number = 0;

  // This function queries the wizards API to look for the card
  findVersions(name: string) : void {
    
  }
  
  add(name: string, cardSet: string, cardCount:string, foil:boolean, multiverseID:number = 0): void {
    name = name.trim();
    cardSet = cardSet.trim();
    icount = 1;

    var icount = 0;
    if (!name) { return; }
    // seeing how cardCount unfortunately is not a number, we need to parse it
    if (cardCount) { icount = +cardCount; } 

    let cardVer : CardVersion = {"card_count" : icount, "foil" : foil, "multiverseID" : multiverseID};

    if (cardSet) {cardVer["set_code"] = cardSet; }
    
    this.collecteDBService.postNewCard({ name, "versions" : [cardVer] } as APICard).subscribe(hero => {
      this.goBack();
    });
  }

  goBack(): void {
    this.location.back();
  }
}
