import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  firstName: string;
  lastName: string;
  phone1: number;
  email1: string;
  password1: string;
  confirmPassword: string;
  //error messaging
  errorMsgFirstName = "";
  errorMsgLastName: "";
  errorMsgPhone: "";
  errorMsgEmail: "";
  errorMsgPassword: "";
  errorMsgConfirmPassword: "";

  constructor() { }

  ngOnInit() {
  }
  


  //these two lines are temporary 
  //submitted = false;

  //ngSubmit() { this.submitted = true; }

}
