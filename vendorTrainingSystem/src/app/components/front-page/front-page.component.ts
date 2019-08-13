import { LoginComponent } from './../../modals/login/login.component';
<<<<<<< HEAD
import { AboutComponent } from './../../modals/about/about.component';
=======
import { UserEditComponent } from './../../modals/user-edit/user-edit.component';
import { DeleteProfileComponent } from './../../modals/delete-profile/delete-profile.component';
>>>>>>> 67320510ab7ca86ddd8e319f94ad620079e0e41a
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
    

  constructor(private modalService:NgbModal) { }

  ngOnInit() {
  }

<<<<<<< HEAD
  openModal(){
    let modalReg = this.modalService.open(AboutComponent);
=======
  openLoginModal(){
    let modalReg = this.modalService.open(LoginComponent);
>>>>>>> 67320510ab7ca86ddd8e319f94ad620079e0e41a
  }
  
  openRegisterModal(){
    let modalReg = this.modalService.open(RegisterComponent);
  }
  
  // open(component: Component) {
  //   let modalReg = this.modalService.open(component);
  // }

}
