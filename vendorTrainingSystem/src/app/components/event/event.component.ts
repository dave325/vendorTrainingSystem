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
        backgroundColor: "#ff000085"
      })),
      state('closed', style({
        // height: '10px',
        width: "1%",
        opacity: 0.5,
        backgroundColor: 'green'
      })),
      transition('open => closed', [
        animate('.5s')
      ]),
      transition('closed => open', [
        animate('.5s')
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

  // swap between col-12 and col-3 to give the animation effect -Ed
  toggle(){
    this.isOpen = !this.isOpen;
    if(this.isOpen){
      //this.classListNames  = "col-12"
    }
    else{
      this.classListNames = "col-md-3"
    }
  }

  props: {

  }

  @Input() event:Event;


  ngOnInit() {
  }

}
