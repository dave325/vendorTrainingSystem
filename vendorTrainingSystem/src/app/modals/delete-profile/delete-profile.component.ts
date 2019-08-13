import { HttpClient } from '@angular/common/http';
import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UserService } from 'src/app/user.service';

@Component({
  selector: 'dsol-delete-profile',
  templateUrl: './delete-profile.component.html',
  styleUrls: ['./delete-profile.component.css']
})
export class DeleteProfileComponent implements OnInit {
  user_info = {
    username: <string> null,
    password: <string> null,

  }
  constructor(
    public modalService: NgbModal,
    private userService: UserService,
    private http:HttpClient) { }

  ngOnInit() {
  }

  onSubmitTemplateBased(){
    this.http.post('/api/user/profileDelete/',this.user_info).toPromise().then(
      (res) =>{
        console.log(res)
      }
    )
  }
}
