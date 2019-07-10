import { Component, OnInit } from '@angular/core';
import {globals} from '../../globals'

@Component({
  selector: 'dsol-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {
  name: String;
  address: String;
  phoneNumber: String;
  email: String;
  editing: Boolean;
  constructor() {
    this.editing = false;
    this.name="Google LLC";
    this.address="1600 Amphitheatre Parkway, Mountain View, CA 94043, USA";
    this.phoneNumber="123-503-4867",
    this.email="ContactGoogle@gmail.com"
   }

  ngOnInit() {
  }

  editConfirm(){
    if(!globals.regExTests.emailRegex.test(name)){

    }
    this.editing=false;
    //ask for confirmation from database
  }

}
