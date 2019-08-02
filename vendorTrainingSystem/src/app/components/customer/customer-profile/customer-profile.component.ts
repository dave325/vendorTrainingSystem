import { Component, OnInit } from '@angular/core';
import { Event } from '../../../models/Event';
import { dummy_events } from '../../../dummy-data/dummy-events';

@Component({
  selector: 'app-customer-profile',
  templateUrl: './customer-profile.component.html',
  styleUrls: ['./customer-profile.component.css']
})
export class CustomerProfileComponent implements OnInit {

  Events:Event[] = dummy_events;
  
  constructor() { }

  ngOnInit() {
  }

}
