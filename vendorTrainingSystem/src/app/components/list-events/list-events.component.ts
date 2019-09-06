import { Component, OnInit } from '@angular/core';
import { Event } from '../../models/Event';
import { dummy_events } from '../../dummy-data/dummy-events';

@Component({
  selector: 'app-list-events',
  templateUrl: './list-events.component.html',
  styleUrls: ['./list-events.component.css']
})
export class ListEventsComponent implements OnInit {

  Events = dummy_events;

  constructor() { }

  ngOnInit() {
  }

}
