import { Component, OnInit } from '@angular/core';
import {globals} from '../../globals'

@Component({
  selector: 'dsol-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
  name: string;
  phoneNumber: string;
  email: string;
  editing: boolean;
  //probably temporary solution to error messaging
  errorMsgName: string; 
  errorMsgPhoneNumber: string;
  errorMsgEmail: string;

  constructor() {
    this.editing = false;
    this.name="Google LLC";
    this.phoneNumber="123-503-4867";
    this.email="ContactGoogle@gmail.com";
    //error messaging
    this.errorMsgName = "";
    this.errorMsgPhoneNumber = "";
    this.errorMsgEmail = "";

   }

  ngOnInit() {
    
  }

  editConfirm(){
    let valid: boolean;
    valid = true;

    if(!globals.regExTests.emailRegex.test(this.email)){
      this.errorMsgEmail = "Invalid Email Address";
      valid = false;
    }else{
      this.errorMsgEmail = "";
    }
    if(!globals.regExTests.phoneRegex.test(this.phoneNumber)){
      this.errorMsgPhoneNumber="Invalid Phone Number";
      valid = false;
    }else{
      this.errorMsgPhoneNumber = "";
    }
    if(this.name === ""){
      this.errorMsgName = "Name field cannot be empty";
      valid = false;
    }else{
      this.errorMsgName = "";
    }
    
    if(valid){
      this.editing=false;
      //ask for confirmation from database
    }
    
  }

}
