import { Component, OnInit, Input, HostBinding } from '@angular/core';
import { trigger, state, style, animate, transition } from '@angular/animations';



import { Event } from '../../models/Event';
import { EventModalComponent } from 'src/app/modals/event-modal/event-modal.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';



@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css'],
  host: { "[class]": "classListNames" },
  animations: [
    //animations go here
    trigger('openClose', [
      // ...
      state('open', style({
        height: '200px',
        width: "100%",
        opacity: 1,
        backgroundColor: "#ff000085"
      })),
      state('closed', style({
        // height: '10px',
        width: "1%",
        opacity: 1,
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
  constructor(private modalService: NgbModal) {
    this.classListNames = this.cn;
  }

  open(content) {
    this.modalService.open(content).result.then((result) => {
      
    }, (reason) => {

    });
  }

  // swap between col-12 and col-3 to give the animation effect -Ed
  toggle() {
    this.isOpen = !this.isOpen;
    if (this.isOpen) {
      this.classListNames  = "col-12"
    }
    else {
      this.classListNames = "col-md-3"
    }
  }


  @Input() event: Event;


  ngOnInit() {
  }

}
