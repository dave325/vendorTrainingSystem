import { AuthenticationService } from './../../services/Authentication.service';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'dsol-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  register = { 
    username: <string> null,
    firstName: <string> null,
    lastName: <string> null,
    phone: <number> null,
    address: <string> null,
    email: <string> null,
    password: <string> null,
    confirmPassword: <string> null,
    role_id:<number> 1,
    vendor_name:<string> null,
    vendor_email: <string> null,
    vendor_address: <string> null,
    vendor_phone: <string> null,
  //error messaging
  errorMsgFirstName: "You must enter a valid First Name",
  errorMsgLastName: "You must enter a valid Last Name",
  errorMsgPhone: "You must enter a valid Phone Number",
  errorMsgEmail: "You must enter a valid Email",
  errorMsgPassword: "You must enter a valid Password",
  errorMsgConfirmPassword: "Passwords do not match",
  }
  isVendor:Boolean = false;
  error = null;
  info = null;
  constructor(
    public modalService: NgbActiveModal,
    private userService: UserService,
    private auth: AuthenticationService
    ) { }

  ngOnInit() {
  }
  
  onSubmitTemplateBased(){
    if(this.isVendor){
      this.register.role_id = 2;
    }else{
      this.register.role_id = 1;
    }
    console.log(this.register)
    this.auth.register(this.register).then(
      (res) =>{
        this.error = null;
        this.info = "Successfully Registered!"
        console.log(res)
      },
      (err) =>{
        this.info = null;
        this.error = "Error logging in, please try again!";
        console.log(err)
      }
    );
    /*
    this.http.post('/api/user/register/',this.register).toPromise().then(
      (res) =>{
        console.log(res)
      }
    )
    /
    this.userService.getUser(this.register).then(
      (res) =>{
        console.log("success")
      },
      (err)=>{
        console.log("error")
      }
    )
    */
  }
}
