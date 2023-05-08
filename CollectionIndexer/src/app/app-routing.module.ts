import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CardComponent } from './card/card.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CardDetailComponent } from './card-detail/card-detail.component';
import { AddCardComponent } from './add-card/add-card.component';

const routes: Routes = [
  { path: '', redirectTo: '/cards', pathMatch: 'full' },
  { path: 'detail/:id', component: CardDetailComponent },
  { path: 'cards', component: CardComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'new-card', component: AddCardComponent } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }