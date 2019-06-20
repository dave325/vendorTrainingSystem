import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CustomerComponent } from './components/customer/customer.component';
import { CustomerProfileComponent } from './components/customer/customer-profile/customer-profile.component';
import { VendorComponent } from './components/vendor/vendor.component';
import { VendorProfileComponent } from './components/vendor/vendor-profile/vendor-profile.component';
import { AdminComponent } from './components/admin/admin.component';
import { AdminProfileComponent } from './components/admin/admin-profile/admin-profile.component';
import { FrontPageComponent } from './components/front-page/front-page.component';
import { ListEventsComponent } from './components/list-events/list-events.component';

@NgModule({
  declarations: [
    AppComponent,
    CustomerComponent,
    CustomerProfileComponent,
    VendorComponent,
    VendorProfileComponent,
    AdminComponent,
    AdminProfileComponent,
    FrontPageComponent,
    ListEventsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
