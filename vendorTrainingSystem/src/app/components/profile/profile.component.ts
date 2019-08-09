import { Component, OnInit } from '@angular/core';
import { User } from '../../models/User'; //the blueprint
import { dummy_users } from '../../dummy-data/dummy-users'; // the data
import { UserService} from '../../user.service';

@Component({
  selector: 'dsol-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  d_users:User[] = dummy_users;
  info: string = null;
  error: string = null;
  constructor(private userService: UserService) { }

  ngOnInit() {
  }

}
