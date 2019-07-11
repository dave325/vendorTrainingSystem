import { Component, OnInit } from '@angular/core';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'dsol-event-modal',
  templateUrl: './event-modal.component.html',
  styleUrls: ['./event-modal.component.css']
})
export class EventModalComponent implements OnInit {
  closeResult: string;

   constructor() { }

   ngOnInit():void{

   }

}

