import { Component, OnInit, Input } from '@angular/core';
<<<<<<< HEAD
import { NgbActiveModal} from '@ng-bootstrap/ng-bootstrap'
import { HttpClient } from '@angular/common/http'
import { Event } from '../../models/Event';
import { UserService } from 'src/app/user.service'
=======
import { AuthenticationService } from './../../services/Authentication.service';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Event } from '../../models/Event';
//import { EventService} from '../../services/EventService';
>>>>>>> fafa0ac22cd91069dad915ec89f25ad9816acca1

@Component({
  selector: 'dsol-event-edit',
  templateUrl: './event-edit.component.html',
  styleUrls: ['./event-edit.component.css']
})
export class EventEditComponent implements OnInit {

  edit = {
    name: <string> null,
    summary: <string> null,
    description: <string> null,
    start_time: <string> null,
    end_time: <string> null,
  }

  @Input() event;
  constructor(
<<<<<<< HEAD
    activeModal: NgbActiveModal,
    private http: HttpClient,
    private userService: UserService,
    ) { 
=======
    public modalService: NgbModal, 
    //private eventSerivce: EventService,
    private auth: AuthenticationService) { 
>>>>>>> fafa0ac22cd91069dad915ec89f25ad9816acca1
    console.log(this.event);
  }

  ngOnInit() {
  }

  onSubmitTemplateBased() {
    this.http.post('/api/user/eventEdit/', this.edit).toPromise().then(
      (res) => {
        console.log(res)
      }
    )
  }
}
