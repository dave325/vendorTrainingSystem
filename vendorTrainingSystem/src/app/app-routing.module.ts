import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FrontPageComponent } from './components/front-page/front-page.component';
import { CustomerComponent } from './components/customer/customer.component';
import { VendorComponent } from './components/vendor/vendor.component';
import { AdminComponent } from './components/admin/admin.component';
import { ListEventsComponent } from './components/list-events/list-events.component';

import { CustomerProfileComponent } from './components/customer/customer-profile/customer-profile.component';
import { VendorProfileComponent } from './components/vendor/vendor-profile/vendor-profile.component';
import { AdminProfileComponent } from './components/admin/admin-profile/admin-profile.component';

const routes: Routes = [
  { path: '', component: FrontPageComponent },
  { path: 'customer', component: CustomerComponent },
  { path: 'vendor', component: VendorComponent },
  { path: 'admin', component: AdminComponent },
  { path: 'list-events', component: ListEventsComponent }

  // { path: 'customer/profile', component: CustomerProfileComponent },
  // { path: 'vendor/profile', component: VendorProfileComponent },
  // { path: 'admin/profile', component: AdminProfileComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
