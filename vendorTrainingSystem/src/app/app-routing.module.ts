import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// for animations -- Ed
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { FrontPageComponent } from './components/front-page/front-page.component';
import { CustomerComponent } from './components/customer/customer.component';
import { VendorComponent } from './components/vendor/vendor.component';
import { AdminComponent } from './components/admin/admin.component';
import { ListEventsComponent } from './components/list-events/list-events.component';
import { ReportVendorComponent} from './modals/report-vendor/report-vendor.component';
import { ContactInfoComponent} from './components/contact-info/contact-info.component';


const routes: Routes = [
  { path: '', component: FrontPageComponent },
  { path: 'customer', component: CustomerComponent },
  { path: 'vendor', component: VendorComponent },
  { path: 'admin', component: AdminComponent },
  { path: 'list-events', component: ListEventsComponent },
  { path: 'reportVendor', component: ReportVendorComponent },
  { path: 'contact', component: ContactInfoComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes),
    BrowserModule,
    BrowserAnimationsModule],
  exports: [RouterModule]
})
export class AppRoutingModule { }
