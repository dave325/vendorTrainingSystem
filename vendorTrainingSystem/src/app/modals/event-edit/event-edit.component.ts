import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal} from '@ng-bootstrap/ng-bootstrap'
import { HttpClient } from '@angular/common/http'
import { Event } from '../../models/Event';
import { UserService } from 'src/app/user.service'

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
    activeModal: NgbActiveModal,
    private http: HttpClient,
    private userService: UserService,
    ) { 
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
