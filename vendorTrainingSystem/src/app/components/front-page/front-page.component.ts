import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterComponent } from '../../modals/register/register.component'
import { LoginComponent } from '../../modals/login/login.component'


@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.css']
})
export class FrontPageComponent implements OnInit {
  rc = RegisterComponent;
  lc = LoginComponent;

  constructor(private modalService: NgbModal) { }

  ngOnInit() {
  }

  open(component: Component) {
    let modalReg = this.modalService.open(component);
  }

}
