import { Component, OnInit } from '@angular/core';
import { environment } from '../../../environments/environment'

interface ContactInfoModel{
  vendorName: string;
  phoneNumber: string;
  email: string;
}

@Component({
  selector: 'app-contact-info',
  templateUrl: './contact-info.component.html',
  styleUrls: ['./contact-info.component.css']
})
export class ContactInfoComponent implements OnInit {
  contactModel = <ContactInfoModel>{};
  editing: boolean = false;
  emailRegex = environment.regExTests.emailRegex;
  phoneRegex = environment.regExTests.phoneRegex;
  constructor() {
    
    this.contactModel.vendorName="Google LLC";
    this.contactModel.phoneNumber="123-503-4867";
    this.contactModel.email="ContactGoogle@gmail.com";
  }
  

  ngOnInit() {
    
  }

  editConfirm(){
    let valid: boolean = true;
    
    if(!this.emailRegex.test(this.contactModel.email)){
      
      valid = false;
    }
    if(!this.phoneRegex.test(this.contactModel.phoneNumber)){
      
      valid = false;
    }
    if(this.contactModel.vendorName === ""){
      
      valid = false;
    }
    
    if(valid){
      this.editing=false;
      alert("name: "+ this.contactModel.vendorName+", phoneNumber: "+ this.contactModel.phoneNumber+ ", email: "+this.contactModel.email);
      //ask for confirmation from database
    }
    
  }

}
