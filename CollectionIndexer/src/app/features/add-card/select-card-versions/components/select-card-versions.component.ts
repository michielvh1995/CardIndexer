import { Component, Input } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

import { APICard } from 'src/app/shared/models/api';
import { WizardsAPIService } from 'src/app/shared/wizardsAPI/wizards-api.service';

@Component({
  selector: 'app-select-card-versions',
  templateUrl: '../pages/select-card-versions.component.html',
  styleUrls: ['../pages/select-card-versions.component.css']
})
export class SelectCardVersionsComponent {
  constructor(
    private wizardsAPIService : WizardsAPIService
    ) { }
    
    queriedCards? : APICard[];
    selectedCards? : APICard[];

    submitted = false;

    @Output() addCardsEvent  = new EventEmitter<APICard[]>();

    @Input() success = false;

    cardSelectorForm = new FormGroup({
      cardNameControl: new FormControl(''),
      cardSetControl: new FormControl('')
    });

    onCardSearch() {
      console.warn(this.cardSelectorForm.value);
  
      var cardName = this.cardSelectorForm.value.cardNameControl?.trim().toLowerCase();
      var cardSet = this.cardSelectorForm.value.cardSetControl?.trim().toLowerCase();
  
      if(!cardName && !cardSet) return;
  
      this.wizardsAPIService.queryCardsByNameAndSet(cardName, cardSet)
      .subscribe(fetched => {
        if(fetched.length) this.queriedCards = fetched;

        this.selectedCards = this.queriedCards; // TMP DEBUG
      });
    }


    // These variables are used to display how many cards are added:
    cardCount = 0;

    addSelection() {
      if(!this.selectedCards) return;
      // Calculate the card count:

      for (let i = 0; i < this.selectedCards.length; i++)
        for (let j = 0; j < this.selectedCards[i].versions.length; j++)
          this.cardCount += this.selectedCards[i].versions[j].card_count;
        
      console.log(this.cardCount);

      this.addCardsEvent.emit(this.selectedCards);
      this.submitted = true;
    }
}
