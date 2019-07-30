import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'dsol-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  login = {
    email:<string> null,
    password: <string> null
  }
    

  constructor(public modalService: NgbModal) { }



 

  ngOnInit() {
  }


}
