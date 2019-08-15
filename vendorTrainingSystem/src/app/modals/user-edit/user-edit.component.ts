import { Component, OnInit, Input } from '@angular/core';
import { NgbModal, NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { UserService } from 'src/app/user.service';
import { AuthenticationService} from '../../services/Authentication.service';
@Component({
  selector: 'dsol-user-edit',
  templateUrl: './user-edit.component.html',
  styleUrls: ['./user-edit.component.css']
})
export class UserEditComponent implements OnInit {

  edit = {
    username: <string> null,
    address: <string> null,
    phone: <string> null,
    email: <string> null,
    password: <string> null,
    newPassword: <string> null
  }
  info = null;
  error = null;
  constructor(
    public modalService: NgbModal,
    private userService: UserService,
    private auth: AuthenticationService
  ) { }

  ngOnInit() {
  }

  onSubmitTemplateBased() {
    console.log(this.edit)
    
    this.auth.editProfile(this.edit).then(
      (res) =>{
        this.error = null;
        this.info = "Successfully edited!"
        console.log(res)
      },
      (err) =>{
        this.info = null;
        this.error = "Editing error, please try again!";
        console.log(err)
      }
    );
    /*
    this.userService.getUser(this.edit).then(
      (res) => {
        console.log("success")
      },
      (err) => {
        console.log("error")
      }
    )
    */
  }

}
