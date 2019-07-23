import { Component, OnInit } from '@angular/core';
import { User } from '../../models/User'; //the blueprint
import { dummy_users } from '../../dummy-data/dummy-users'; // the data

@Component({
  selector: 'dsol-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  d_users:User[] = dummy_users;

  constructor() { }

  ngOnInit() {
  }

}
