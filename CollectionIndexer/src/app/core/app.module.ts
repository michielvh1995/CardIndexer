import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { FormsModule } from '@angular/forms'

import { AppComponent } from './components/app.component';
import { CardComponent } from '../features/card/components/card.component';
import { CardDetailComponent } from '../card-detail/card-detail.component';
import { MessagesComponent } from '../shared/messages/components/messages.component';
import { AppRoutingModule } from './app-routing.module';
import { DashboardComponent } from '../features/dashboard/components/dashboard.component';
import { SharedModule } from '../shared/shared.module';
import { FeaturesModule } from '../features/features.module';


@NgModule({
  declarations: [
    AppComponent,
    CardComponent,
    CardDetailComponent,
    MessagesComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    SharedModule,
    FeaturesModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
