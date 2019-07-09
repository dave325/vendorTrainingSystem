import { Component, OnInit, Input, HostBinding } from '@angular/core';
import { trigger, state, style, animate, transition } from '@angular/animations';

import { Event } from '../../models/Event';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css'],
  host:{ "[class]" : "classListNames"},
  animations:[
    //animations go here
    trigger('openClose', [
      // ...
      state('open', style({
        height: '200px',
        width : "100%",
        opacity: 1,
        backgroundColor: 'yellow'
      })),
      state('closed', style({
        height: '100px',
        width: "25%",
        opacity: 0.5,
        backgroundColor: 'green'
      })),
      transition('open => closed', [
        animate('1s')
      ]),
      transition('closed => open', [
        animate('0.5s')
      ]),
    ]),
  ]
})

export class EventComponent implements OnInit {

  isOpen = false;
  classListNames;
  cn = "col-12 col-md-3";;
  constructor(){
    this.classListNames = this.cn;
  }
  toggle(){
    this.isOpen = !this.isOpen;
    if(this.isOpen){
      this.classListNames  = "col-12"
    }
    else{
      this.classListNames = "col-md-3"
    }
  }

  props: {

  }

  @Input() event:Event;

  constructor() { }

  ngOnInit() {
  }

}
