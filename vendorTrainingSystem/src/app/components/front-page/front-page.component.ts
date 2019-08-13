import { LoginComponent } from './../../modals/login/login.component';
import { UserEditComponent } from './../../modals/user-edit/user-edit.component';
// import { DeleteProfileComponent } from './../../modals/delete-profile/delete-profile.component';
import { Component, OnInit } froogin/login.component'
// import { ReportVendorComponent} from '../../modalm '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
<<<<<<< HEAD
// import { RegisterComponent } from '../../modals/register/register.component'
// import { LoginComponent } from '../../modals/ls/report-vendor/report-vendor.component'
// import { EventEditComponent} from '../../modals/event-edit/event-edit.component'
=======
import { RegisterComponent } from '../../modals/register/register.component'
import { ReportVendorComponent} from '../../modals/report-vendor/report-vendor.component'
import { EventEditComponent} from '../../modals/event-edit/event-edit.component'
>>>>>>> 2c84f3a3729d8241675c127fcef37f1777226dce

@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.css']
})
export class FrontPageComponent implements OnInit {
  // eventEditComponent = EventEditComponent;
  // deleteProfileComponent = DeleteProfile;
    userEditComponent = UserEditComponent;

  constructor(private modalService:NgbModal) { }

  ngOnInit() {
  }

  openLoginModal(){
    let modalReg = this.modalService.open(LoginComponent);
    let modalEdit = this.modalService.open(UserEditComponent);
    // letmodalDelete = this.modalService.open.(DeleteProfileComponent);
  }
  
  openRegisterModal(){
    let modalReg = this.modalService.open(RegisterComponent);
  }
  
  // open(component: Component) {
  //   let modalReg = this.modalService.open(component);
  // }

}
