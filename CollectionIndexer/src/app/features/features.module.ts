import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { AddCardComponent } from './add-card/components/add-card.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SharedModule } from '../shared/shared.module';
import { SelectCardVersionsComponent } from './add-card/select-card-versions/components/select-card-versions.component';



@NgModule({
  declarations: [
    AddCardComponent,
    SelectCardVersionsComponent,
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
