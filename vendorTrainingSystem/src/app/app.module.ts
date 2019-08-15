import { AuthenticationService } from './services/Authentication.service';
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
import { ReportVendorComponent } from './modals/report-vendor/report-vendor.component';
import { RegisterComponent } from './modals/register/register.component';
import { LoginComponent } from './modals/login/login.component';
import { EventModalComponent } from './modals/event-modal/event-modal.component';
import { AboutComponent } from './modals/about/about.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { EventEditComponent } from './modals/event-edit/event-edit.component';
import { ProfileComponent } from './components/profile/profile.component';
import { HttpClientModule } from '@angular/common/http';
import { UserEditComponent } from './modals/user-edit/user-edit.component';
import { DeleteProfileComponent } from './modals/delete-profile/delete-profile.component';
import { EditVendorProfileComponent } from './modals/edit-vendor-profile/edit-vendor-profile.component';
import { AdminService } from './services/AdminService';
import { EventService } from './services/EventService';

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
    NavbarComponent,
    ReportVendorComponent,
    LoginComponent,
    EventModalComponent,
    AboutComponent,
    EventModalComponent,
    EventEditComponent,
    RegisterComponent,
    ProfileComponent,
    LoginComponent,
    UserEditComponent,
    DeleteProfileComponent,
    EditVendorProfileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    NgbModule
  ],
  entryComponents: [AboutComponent, EventEditComponent, DeleteProfileComponent, UserEditComponent, EventModalComponent,RegisterComponent, ReportVendorComponent,  AboutComponent, EventEditComponent, LoginComponent, EditVendorProfileComponent],
  providers: [AuthenticationService, AdminService, EventService],
  bootstrap: [AppComponent]
})
export class AppModule { }
