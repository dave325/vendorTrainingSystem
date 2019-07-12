import { Component, OnInit } from '@angular/core';
import { environment} from '../../../../environments/environment'
interface AdminProfileModel{
  vendorName: string,
  email: string,
  phoneNumber: string
}

@Component({
  selector: 'app-admin-profile',
  templateUrl: './admin-profile.component.html',
  styleUrls: ['./admin-profile.component.css']
})
export class AdminProfileComponent implements OnInit {
  adminProfileModel = <AdminProfileModel>{};
  editing: boolean = false;
  phoneRegex = environment.regExTests.phoneRegex;
  emailRegex = environment.regExTests.emailRegex;
  constructor() {
    this.adminProfileModel.vendorName = "curlfest";
    this.adminProfileModel.email = "sdsds@gmail.com";
    this.adminProfileModel.phoneNumber = "123-456-7890";
  }
  
  ngOnInit() {
  }

  onSubmitConfirm(){
    let valid:boolean = true;
    console.log(this.adminProfileModel.vendorName)
    if(this.adminProfileModel.vendorName === ""){//trim before check
      valid = false;
    }
    if(!this.phoneRegex.test(this.adminProfileModel.phoneNumber) && !(this.adminProfileModel.phoneNumber === '')){
      valid = false;
    }
    if(!this.emailRegex.test(this.adminProfileModel.email)  && !(this.adminProfileModel.email === '')){
      valid = false;
    }
    if(valid){
      alert("name: "+ this.adminProfileModel.vendorName+", phoneNumber: "+ this.adminProfileModel.phoneNumber+ ", email: "+this.adminProfileModel.email);
      this.editing = false;
    }
    
  }

}
