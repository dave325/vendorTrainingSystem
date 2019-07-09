import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FrontPageComponent } from './components/front-page/front-page.component';
import { CustomerComponent } from './components/customer/customer.component';
import { VendorComponent } from './components/vendor/vendor.component';
import { AdminComponent } from './components/admin/admin.component';
import { ListEventsComponent } from './components/list-events/list-events.component';
<<<<<<< HEAD
// import { RegisterComponent } from './modal/register.component';

=======
import { ReportVendorComponent} from './modals/report-vendor/report-vendor.component'
>>>>>>> db18624487dad9d69a8b8051cc76b72a0da2f37f

const routes: Routes = [
  { path: '', component: FrontPageComponent },
  { path: 'customer', component: CustomerComponent },
  { path: 'vendor', component: VendorComponent },
  { path: 'admin', component: AdminComponent },
  { path: 'list-events', component: ListEventsComponent },
  {path: 'reportVendor', component: ReportVendorComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
