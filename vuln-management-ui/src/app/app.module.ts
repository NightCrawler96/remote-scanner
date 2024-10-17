import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TargetsComponent } from './components/targets/targets.component';
import { ServicesComponent } from './components/services/services.component';
import { VulnerabilitiesComponent } from './components/vulnerabilities/vulnerabilities.component';

@NgModule({
  declarations: [
    AppComponent,
    TargetsComponent,
    ServicesComponent,
    VulnerabilitiesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
