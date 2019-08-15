import { LoginComponent } from './../../modals/login/login.component';
import { EventModalComponent } from './../../modals/event-modal/event-modal.component';
import { UserEditComponent } from './../../modals/user-edit/user-edit.component';
import { DeleteProfileComponent } from './../../modals/delete-profile/delete-profile.component';
import { Component, OnInit } from '@angular/core';
// import { ReportVendorComponent} from '../../modalm '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterComponent } from '../../modals/register/register.component'
import { ReportVendorComponent} from '../../modals/report-vendor/report-vendor.component'

@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.css']
})
export class FrontPageComponent implements OnInit {

  constructor(private modalService:NgbModal) { }

  ngOnInit() {
  }
  
  openEventModal(){
    let modalReg = this.modalService.open(EventModalComponent);
  }
  openLoginModal(){
    let modalReg = this.modalService.open(LoginComponent);
  }
  openRegisterModal(){
    let modalReg = this.modalService.open(RegisterComponent);
  }
  

  // open(component: Component) {
  //   let modalReg = this.modalService.open(component);
  // }

}
