import { Component, OnInit } from '@angular/core';

interface AdminProfileModel{
  firstName: string,
  lastName: string,
  email: string,
  phoneNumber: string,
  password: string
}

@Component({
  selector: 'app-admin-profile',
  templateUrl: './admin-profile.component.html',
  styleUrls: ['./admin-profile.component.css']
})
export class AdminProfileComponent implements OnInit {
  adminProfileModel = <AdminProfileModel>{};
  Editing: boolean = false;
  constructor() {
    this.adminProfileModel.firstName = "John";
    this.adminProfileModel.lastName = "Smith";
    this.adminProfileModel.email = "sdsds@gmail.com";
    this.adminProfileModel.phoneNumber = "123-456-7890";
    this.adminProfileModel.password = "hello123";
  }
  
  ngOnInit() {
  }

}
