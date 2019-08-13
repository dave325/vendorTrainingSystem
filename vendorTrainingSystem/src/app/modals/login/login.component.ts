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

  constructor(
    public modalService: NgbModal,
    private userService: UserService,
    private http:HttpClient
    ) { }

  ngOnInit() {
  }

  onSubmitTemplateBased(){
    this.http.post('/api/user/login/',this.login).toPromise().then(
      (res) =>{
        console.log(res)
      }
    )
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
