import { Component, OnInit } from '@angular/core';
import { NgbModal, NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { UserService } from 'src/app/user.service';
import { AuthenticationService } from '../../services/Authentication.service';

@Component({
  selector: 'dsol-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {
  about = {
  vendorAddress: <string> null,
  vendorPhone: <string> null,
  vendorEmail: <string> null,
  }
  constructor(
    public modalService: NgbModal, 
    private userService: UserService,
    private auth: AuthenticationService
  ) { }

  ngOnInit() {
  }

}
