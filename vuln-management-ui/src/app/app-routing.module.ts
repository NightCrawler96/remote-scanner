import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TargetsComponent } from './components/targets/targets.component';
import { ServicesComponent } from './components/services/services.component';
import { VulnerabilitiesComponent } from './components/vulnerabilities/vulnerabilities.component';

const routes: Routes = [
  { path: 'targets', component: TargetsComponent },
  { path: 'services', component: ServicesComponent },
  { path: 'vulnerabilities', component: VulnerabilitiesComponent },
  { path: '', redirectTo: '/targets', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
