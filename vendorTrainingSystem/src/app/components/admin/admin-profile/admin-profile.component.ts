import { Component, OnInit } from '@angular/core';
import { environment} from '../../../../environments/environment'
import { Admin } from '../../../models/Admin'
import { Event } from '../../../models/Event';
import { dummy_events } from '../../../dummy-data/dummy-events';
import { Vendor } from '../../../models/Vendor';
import { dummy_vendors } from '../../../dummy-data/dummy-vendors';

@Component({
  selector: 'app-admin-profile',
  templateUrl: './admin-profile.component.html',
  styleUrls: ['./admin-profile.component.css']
})
export class AdminProfileComponent implements OnInit {
  Events:Event[] = dummy_events;
  Vendors:Vendor[] = dummy_vendors;


  adminProfileModel = <Admin>{};
  editing: boolean = false;
  phoneRegex = environment.regExTests.phoneRegex;
  emailRegex = environment.regExTests.emailRegex;
  constructor() {
    this.adminProfileModel.name = "curlfest";
    this.adminProfileModel.email = "sdsds@gmail.com";
    this.adminProfileModel.phone = "123-456-7890";
  }
  
  ngOnInit() {
  }

  onSubmitConfirm(){
    let valid:boolean = true;
    console.log(this.adminProfileModel.name)
    if(this.adminProfileModel.name === ""){//trim before check
      valid = false;
    }
    if(!this.phoneRegex.test(this.adminProfileModel.phone) && !(this.adminProfileModel.phone === '')){
      valid = false;
    }
    if(!this.emailRegex.test(this.adminProfileModel.email)  && !(this.adminProfileModel.email === '')){
      valid = false;
    }
    if(valid){
      alert("name: "+ this.adminProfileModel.name+", phoneNumber: "+ this.adminProfileModel.phone+ ", email: "+this.adminProfileModel.email);
      this.editing = false;
    }
    
  }

}
