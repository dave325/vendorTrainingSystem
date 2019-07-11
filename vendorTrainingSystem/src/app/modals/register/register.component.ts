import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  //these two lines are temporary 
  submitted = false;

  ngSubmit() { this.submitted = true; }

}
