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
    private http: HttpClient,
    private eventService: EventService,
    ) { 
    console.log(this.event);
  }

  ngOnInit() {
  }

  onSubmitTemplateBased() {
    this.http.post('/api/vendor/editMyEvents/', this.event).toPromise().then(
      (res) => {
        console.log(res)
      }
    )
  }
}
