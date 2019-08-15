import { Component, OnInit, Input } from '@angular/core';

import { AuthenticationService } from './../../services/Authentication.service';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { EventService} from '../../services/EventService';
import { HttpClient } from '@angular/common/http'
import { Event } from '../../models/Event';

@Component({
  selector: 'dsol-event-edit',
  templateUrl: './event-edit.component.html',
  styleUrls: ['./event-edit.component.css']
})
export class EventEditComponent implements OnInit {
  @Input() event;
  
  constructor(
    activeModal: NgbActiveModal,
    private eventService: EventService,
    ){ 
      console.log(this.event);
    }
  info = null;
  error = null;
  ngOnInit() {
  }

  onSubmitTemplateBased() {
    
    this.eventService.editEvent(this.event).then(
      (res) =>{
        this.error = null;
        this.info = "Edit Successful!"
        console.log(res)
      },
      (err) =>{
        this.info = null;
        this.error = "Error logging in, please try again!";
        console.log(err)
      }
    );
  }
}
