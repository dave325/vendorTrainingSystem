import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  email1: string;
  password1: string;
  //for error messaging 
  errorMsgEmail: "";
  errorMsgPassword: "";

  constructor() { }

  ngOnInit() {
    /*these are temporary 
  submitted = false;

  ngSubmit() { this.submitted = true; }
  */
  }

}
