import { LoginComponent } from './../../modals/login/login.component';
import { AboutComponent } from './../../modals/about/about.component';
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

  openAboutModal(){
    let modalReg = this.modalService.open(AboutComponent);
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

  openReportVendorModal(){
    let modalReg = this.modalService.open(ReportVendorComponent);
  }
  
  openEditVendorProfileModal(){
    let modalReg = this.modalService.open(ReportVendorComponent);
  }
  

  // open(component: Component) {
  //   let modalReg = this.modalService.open(component);
  // }

}
