import { Component, OnInit } from '@angular/core';
import { environment } from '../../../environments/environment'
import { UserService} from '../../user.service';
import {Vendor} from '../../models/Vendor'

@Component({
  selector: 'app-contact-info',
  templateUrl: './contact-info.component.html',
  styleUrls: ['./contact-info.component.css']
})
export class ContactInfoComponent implements OnInit {
  contactModel = <Vendor>{};
  editing: boolean = false;
  emailRegex = environment.regExTests.emailRegex;
  phoneRegex = environment.regExTests.phoneRegex;
  addressRegex = environment.regExTests.addressRegex;

  info: string = null;
  error: string = null;
  constructor(private userService: UserService) {
    
    this.contactModel.name="Google LLC";
    this.contactModel.phone="123-503-4867";
    this.contactModel.email="ContactGoogle@gmail.com";
    this.contactModel.address="123 Hollow St, Queens, New York 86351"
  }
  

  ngOnInit() {
    
  }

  editConfirm(){
    let valid: boolean = true;
    
    if(!this.emailRegex.test(this.contactModel.email)){
      
      valid = false;
    }
    if(!this.phoneRegex.test(this.contactModel.phone)){
      
      valid = false;
    }
    if(this.contactModel.name === ""){
      
      valid = false;
    }
    
    if(valid){
      this.editing=false;
      alert("name: "+ this.contactModel.name+", phone: "+ this.contactModel.phone+ ", email: "+this.contactModel.email+", address: "+this.contactModel.address);
      //ask for confirmation from database
    }
    
  }

}
