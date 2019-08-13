import { Component, OnInit, Input } from '@angular/core';
import { HttpClient} from '@angular/common/http'
import {NgbModal, NgbActiveModal} from '@ng-bootstrap/ng-bootstrap'
import {UserService} from 'src/app/user.service'

@Component({
  selector: 'dsol-user-edit',
  templateUrl: './user-edit.component.html',
  styleUrls: ['./user-edit.component.css']
})
export class UserEditComponent implements OnInit {
  
  edit = {
    username: <string> null,
    email: <string> null,
    password: <string> null,
  }

  constructor(
    public modalService: NgbModal,
    private userService: UserService,
    private http:HttpClient
  ) { }

  ngOnInit() {
  }

  onSubmitTemplateBased(){
    this.http.post('/api/user/edit/',this.edit).toPromise().then(
      (res) =>{
        console.log(res)
      }
    )
    this.userService.getUser(this.edit).then(
      (res) =>{
        console.log("success")
      },
      (err)=>{
        console.log("error")
      }
    )
  }

}
