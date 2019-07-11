import { Component, OnInit } from '@angular/core';
import { environment } from '../../../environments/environment'

interface ContactInfoModel{
  vendorName: string;
  phoneNumber: string;
  email: string;
  editing: boolean;
}

@Component({
  selector: 'app-contact-info',
  templateUrl: './contact-info.component.html',
  styleUrls: ['./contact-info.component.css']
})
export class ContactInfoComponent implements OnInit {
  contactModel = <ContactInfoModel>{}
  emailRegex = environment.regExTests.emailRegex;
  phoneRegex = environment.regExTests.phoneRegex;
  constructor() {
    this.contactModel.editing = false;
    this.contactModel.vendorName="Google LLC";
    this.contactModel.phoneNumber="123-503-4867";
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
    if(this.contactModel.vendorName === ""){
      
      valid = false;
    }
    
    if(valid){
      this.contactModel.editing=false;
      //ask for confirmation from database
    }
    
  }

}
