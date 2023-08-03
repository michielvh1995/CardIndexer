import { Component } from '@angular/core';
import { Location } from '@angular/common';

import { FormControl, FormGroup } from '@angular/forms';

import { CollectedbService } from 'src/app/shared/collecteDB/collectedb.service';
import { APICard, CardVersion } from 'src/app/shared/models/api';
import { WizardsAPIService } from 'src/app/shared/wizardsAPI/wizards-api.service';
import { Card } from 'src/app/shared/models/card';

@Component({
  selector: 'app-add-card',
  templateUrl: '../pages/add-card.component.html',
  styleUrls: ['../pages/add-card.component.css']
})
export class AddCardComponent {
  constructor(
    private location : Location,
    private collecteDBService : CollectedbService,
    private wizardsAPIService : WizardsAPIService
  ) {
    
   }
  
  multiverseID : number = 0;

  queriedCards? : Card[];
  
  
  multiverseIDControl = new FormControl(0);

  cardSelectorForm = new FormGroup({
    cardNameControl: new FormControl(''),
    cardSetControl: new FormControl('')
  });
  
  onCardSearch() {
    console.warn(this.cardSelectorForm.value);

    var cardName = this.cardSelectorForm.value.cardNameControl?.trim().toLowerCase();
    var cardSet = this.cardSelectorForm.value.cardSetControl?.trim().toLowerCase();

    if(!cardName && !cardSet) return;
    //if(!cardSet) return;

    this.wizardsAPIService.queryCardsByNameAndSet(cardName, cardSet)
    .subscribe(fetched => {
      if(fetched.length) this.queriedCards = fetched;

      // for (let i = 0; i < fetched.length; i++) {
      //   //console.log(`${fetched[i].name}, ${fetched[i].multiverseID}, ${fetched[i].set_code}, ${fetched[i].number}`);
      //   this.queriedCards?.push(fetched[i]);
      // }
    });
  }
  
  add(name   : string, 
      cardSet  : string, 
      cardCount: string, 
      foil     : boolean, 
      multiverseID:number = 0): void 
  {
    name = name.trim();
    cardSet = cardSet.trim();
    icount = 1;

    console.log("add");

    var icount = 0;
    if (!name) { return; }
    // seeing how cardCount unfortunately is not a number, we need to parse it
    if (cardCount) { icount = +cardCount; } 

    let cardVer : CardVersion = {"card_count" : icount, "foil" : foil, "multiverseID" : multiverseID};

    if (cardSet) {cardVer["set_code"] = cardSet; }

    this.wizardsAPIService.getMultiverseIDByNameAndSet(name, cardSet)
      .subscribe(fetched => {
        for (let i = 0; i < fetched.cards.length; i++) {
          console.log(`${fetched.cards[i].name}, ${fetched.cards[i].multiverseid}`);
        }

      });
    
    this.collecteDBService.postNewCard({ name, "versions" : [cardVer] } as APICard).subscribe(_ => {
      this.goBack();
    });
  }

  goBack(): void {
    this.location.back();
  }
}
