import { Component, OnInit, Input } from '@angular/core';

import { Event } from '../../models/Event';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css'],
  host:{"class" : "col-12 col-md-3"}
})
export class EventComponent implements OnInit {

  @Input() event:Event;

  constructor() { }

  ngOnInit() {
  }

}
