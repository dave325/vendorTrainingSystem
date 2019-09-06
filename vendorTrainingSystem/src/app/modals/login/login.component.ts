import { AuthenticationService } from './../../services/Authentication.service';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'dsol-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  login = {
    username:<string> null,
    password: <string> null
  }
  info = null;
  error = null;
  constructor(
    public modalService: NgbActiveModal, 
    private userService: UserService,
    private auth: AuthenticationService
    ) { }

  ngOnInit() {
  }

  onSubmitTemplateBased(){
    console.log(this.login.username)
    console.log(this.login.password)
    this.auth.login(this.login).then(
      (res) =>{
        this.error = null;
        this.info = "Successfully Logged in!"
        console.log(res)
        setTimeout(
          ()=>{
            this.modalService.close();
        }, 300)
        console.log(res)
      },
      (err) =>{
        this.info = null;
        this.error = "Error logging in, please try again!";
        console.log(err)
      }
    );
    /*
    this.userService.getUser(this.login).then(
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
