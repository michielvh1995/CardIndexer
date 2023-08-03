import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { AddCardComponent } from './add-card/components/add-card.component';
import { CardComponent } from './card/components/card.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SharedModule } from '../shared/shared.module';



@NgModule({
  declarations: [
    AddCardComponent,
    //CardComponent
  ],
  imports: [
    CommonModule,
    HttpClientModule,
    SharedModule,
    FormsModule,
    ReactiveFormsModule
  ]
})
export class FeaturesModule { }
