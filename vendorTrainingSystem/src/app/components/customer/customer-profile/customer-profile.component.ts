import { Component, OnInit } from '@angular/core';
import { Event } from '../../../models/Event';
import { dummy_events } from '../../../dummy-data/dummy-events';
import { UserEditComponent } from './../../../modals/user-edit/user-edit.component';
import { DeleteProfileComponent } from './../../../modals/delete-profile/delete-profile.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UserService } from 'src/app/user.service';
@Component({
  selector: 'app-customer-profile',
  templateUrl: './customer-profile.component.html',
  styleUrls: ['./customer-profile.component.css']
})
export class CustomerProfileComponent implements OnInit {
  private customer;
  Events = dummy_events;
  user_info = {
    username: "samsmith123",
    firstname: "Samantha",
    lastname: "Smith",
    phone: "1-800-1234",
    email: "spring123@gmail.com",
    address: "123 York Ave."
  }
  constructor(private modalService:NgbModal,
    private userService: UserService
    ) {
    this.customer = UserService.getUser(); 
  }

  ngOnInit() {
  }

  openUserEditModal() {
    let modalEdit = this.modalService.open(UserEditComponent);
  }

  openDeleteProfileModal() {
    let modalDelete = this.modalService.open(DeleteProfileComponent);
  }

}
