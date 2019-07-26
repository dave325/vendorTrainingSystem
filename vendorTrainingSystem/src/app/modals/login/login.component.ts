import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';


@Component({
  selector: 'dsol-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  email1: string;
  password1: string;

  constructor(public modalService: NgbActiveModal) { }

  ngOnInit() {
  }

  onSubmitTemplateBased(){
    
  }
}
