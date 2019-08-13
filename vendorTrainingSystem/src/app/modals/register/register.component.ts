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
    email: <string> null,
    password: <string> null,
    confirmPassword: <string> null,
  //error messaging
  errorMsgFirstName: "You must enter a valid First Name",
  errorMsgLastName: "You must enter a valid Last Name",
  errorMsgPhone: "You must enter a valid Phone Number",
  errorMsgEmail: "You must enter a valid Email",
  errorMsgPassword: "You must enter a valid Password",
  errorMsgConfirmPassword: "Passwords do not match",
  }

  constructor(
    public modalService: NgbActiveModal,
    private userService: UserService,
    private http:HttpClient
    ) { }

  ngOnInit() {
  }
  
  onSubmitTemplateBased(){
    this.http.post('/api/user/register/',this.register).toPromise().then(
      (res) =>{
        console.log(res)
      }
    )
    /*
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
