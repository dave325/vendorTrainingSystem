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
  errorMsgFirstName = "You must enter a valid First Name";
  errorMsgLastName: "You must enter a valid Last Name";
  errorMsgPhone: "You must enter a valid Phone Number";
  errorMsgEmail: "You must enter a valid Email";
  errorMsgPassword: "You must enter a valid Password";
  errorMsgConfirmPassword: "Passwords do not match";

  constructor() { }

  ngOnInit() {
  }
  
  //these two lines are temporary 
  submitted = false;

  ngSubmit() { this.submitted = true; }

}
