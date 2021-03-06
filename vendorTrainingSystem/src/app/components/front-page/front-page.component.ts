import { LoginComponent } from './../../modals/login/login.component';
import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterComponent } from '../../modals/register/register.component'

@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.css']
})
export class FrontPageComponent implements OnInit {

  constructor(private modalService:NgbModal) { }

  ngOnInit() {
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
