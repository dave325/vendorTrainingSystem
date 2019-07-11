import { Component, OnInit } from '@angular/core';
import { environment } from '../../../environments/environment'

interface ContactInfoModel{
  password1: string;
  email: string;
}

@Component({
  selector: 'dsol-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  contactModel = <ContactInfoModel>{}
  email1: string;
  password1: string;
  //for error messaging 
  errorMsgEmail: "";
  errorMsgPassword: ""; 
  emailRegex = environment.regExTests.emailRegex;
  phoneRegex = environment.regExTests.phoneRegex;

  constructor() { 
    this.contactModel.password1="abc123!";
    this.contactModel.email="ContactGoogle@gmail.com";
  }

  ngOnInit() {
  }

  editConfirm(){
    let valid: boolean = true;
    
    if(!environment.regExTests.emailRegex.test(this.contactModel.email)){
      
      valid = false;
    }
    if(!environment.regExTests.phoneRegex.test(this.contactModel.email)){
      
      valid = false;
    }
    if(this.contactModel.password1 === ""){
      
      valid = false;
    }
    
    
  }

}
