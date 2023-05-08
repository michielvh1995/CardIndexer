import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CardComponent } from '../features/card/components/card.component';
import { DashboardComponent } from '../features/dashboard/components/dashboard.component';
import { CardDetailComponent } from '../card-detail/card-detail.component';
import { AddCardComponent } from '../features/add-card/components/add-card.component';

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