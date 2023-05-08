import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AddCardComponent } from './add-card/components/add-card.component';
import { CardComponent } from './card/components/card.component';



@NgModule({
  declarations: [
    AddCardComponent,
    CardComponent
  ],
  imports: [
    CommonModule
  ]
})
export class FeaturesModule { }
