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
    email:<string> null,
    password: <string> null
  }
  info = null;

  constructor(
    public modalService: NgbModal,
    private userService: UserService
    ) { }



 

  ngOnInit() {
  }

  onSubmitTemplateBased(){
    
    this.userService.getUser(this.login).then(
      (res) =>{
        
      },
      (err)=>{

      }
    )
  }
}
