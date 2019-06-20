import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

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
import { SearchEventComponent } from './components/search-event/search-event.component';
import { EventComponent } from './components/event/event.component';
import { ContactInfoComponent } from './components/contact-info/contact-info.component';
import { NavbarComponent } from './components/header/navbar/navbar.component';

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
    ListEventsComponent,
    SearchEventComponent,
    EventComponent,
    ContactInfoComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
