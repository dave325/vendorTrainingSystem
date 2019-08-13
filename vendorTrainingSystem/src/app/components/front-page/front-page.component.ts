import { LoginComponent } from './../../modals/login/login.component';
import { UserEditComponent } from './../../modals/user-edit/user-edit.component';
import { DeleteProfileComponent } from './../../modals/delete-profile/delete-profile.component';
import { Component, OnInit } from '@angular/core';
// import { ReportVendorComponent} from '../../modalm '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterComponent } from '../../modals/register/register.component'
import { ReportVendorComponent} from '../../modals/report-vendor/report-vendor.component'
import { EventEditComponent} from '../../modals/event-edit/event-edit.component'

@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.css']
})
export class FrontPageComponent implements OnInit {
  // eventEditComponent = EventEditComponent;
    deleteProfileComponent = DeleteProfileComponent;
    userEditComponent = UserEditComponent;

  constructor(private modalService:NgbModal) { }

  ngOnInit() {
  }

  openLoginModal(){
    let modalReg = this.modalService.open(LoginComponent);
  }
  
  openRegisterModal(){
    let modalReg = this.modalService.open(RegisterComponent);
  }

  openUserEditModal() {
    let modalEdit = this.modalService.open(UserEditComponent);
  }

  openDeleteProfileModal() {
    let modalDelete = this.modalService.open(DeleteProfileComponent);
  }
  
  // open(component: Component) {
  //   let modalReg = this.modalService.open(component);
  // }

}
