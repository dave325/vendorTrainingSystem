import { Component, OnInit } from '@angular/core';
import { environment} from '../../../../environments/environment'
interface AdminProfileModel{
  firstName: string,
  lastName: string,
  email: string,
  phoneNumber: string,
  password: string
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
    this.adminProfileModel.firstName = "John";
    this.adminProfileModel.lastName = "Smith";
    this.adminProfileModel.email = "sdsds@gmail.com";
    this.adminProfileModel.phoneNumber = "123-456-7890";
    this.adminProfileModel.password = "hello123";
  }
  
  ngOnInit() {
  }

  onSubmitConfirm(){
    let valid:boolean = true;
    console.log(this.adminProfileModel.firstName)
    if(this.adminProfileModel.firstName === ""){//trim before check
      valid = false;
    }
    if(this.adminProfileModel.lastName === ""){
      valid = false;
    }
    if(this.adminProfileModel.password === ""){ //min req for password?
      valid = false;
    }
    if(!this.phoneRegex.test(this.adminProfileModel.phoneNumber) ){
      valid = false;
    }
    if(!this.emailRegex.test(this.adminProfileModel.email)){
      valid = false;
    }
    if(valid){
      this.editing = false;
    }
    
  }

}
