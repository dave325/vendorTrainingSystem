import { Component, OnInit } from '@angular/core';
import { NgbActiveModal} from '@ng-bootstrap/ng-bootstrap'

import { Event } from '../../models/Event';


@Component({
  selector: 'dsol-event-edit',
  templateUrl: './event-edit.component.html',
  styleUrls: ['./event-edit.component.css']
})
export class EventEditComponent implements OnInit {
  
  constructor(activeModal: NgbActiveModal) { }

  ngOnInit() {
  }

}
