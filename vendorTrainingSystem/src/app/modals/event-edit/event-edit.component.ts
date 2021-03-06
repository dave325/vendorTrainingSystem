import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http'
import { Event } from '../../models/Event';
import { EventService } from "./../../services/EventService.service"

@Component({
  selector: 'dsol-event-edit',
  templateUrl: './event-edit.component.html',
  styleUrls: ['./event-edit.component.css']
})
export class EventEditComponent implements OnInit {
  @Input() event: Event;

  constructor(
    private http: HttpClient,
    activeModal: NgbActiveModal,
    private eventService: EventService
  ) {

    
  }
  info = null;
  error = null;
  ngOnInit() {
    if (!this.event) {
      this.event = <Event>{
        name: '',
        summary: '',
        description: '',
        url: '',
        start_time: '',
        end_time: '',
        add:true
      };
    } else {
      this.event.add = false;
    }
    console.log(this.event);
  }

  onSubmitTemplateBased() {

    this.eventService.editEvent(this.event).then(
      (res) => {
        this.error = null;
        this.info = "Edit Successful!"
        console.log(res)
      },
      (err) => {
        this.info = null;
        this.error = "Error logging in, please try again!";
        console.log(err)
      }
    );

  }
}
