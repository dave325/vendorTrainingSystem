import { Component, OnInit, Input } from '@angular/core';
import { AuthenticationService } from './../../services/Authentication.service';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Event } from '../../models/Event';
//import { EventService} from '../../services/EventService';

@Component({
  selector: 'dsol-event-edit',
  templateUrl: './event-edit.component.html',
  styleUrls: ['./event-edit.component.css']
})
export class EventEditComponent implements OnInit {
  @Input() event;
  constructor(
    public modalService: NgbModal, 
    //private eventSerivce: EventService,
    private auth: AuthenticationService) { 
    console.log(this.event);
  }

  ngOnInit() {
  }

  submit(){
    
  }
}
