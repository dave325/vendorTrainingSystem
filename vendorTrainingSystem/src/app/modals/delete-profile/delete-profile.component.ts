import { HttpClient } from '@angular/common/http';
import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UserService } from 'src/app/user.service';
import { AuthenticationService} from '../../services/Authentication.service';
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
  info = null;
  error = null;
  constructor(
    public modalService: NgbModal, 
    private userService: UserService,
    private auth: AuthenticationService) { }

  ngOnInit() {
  }

  onSubmitTemplateBased(){
    console.log(this.user_info);
    this.auth.deleteProfile(this.user_info).then(
      (res) =>{
        this.error = null;
        this.info = "Successfully deleted!"
        console.log(res)
      },
      (err) =>{
        this.info = null;
        this.error = "Error logging in, please try again!";
        console.log(err)
      }
    )
  }
}
