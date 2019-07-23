import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { RegisterComponent } from '../../modals/register/register.component'
import { LoginComponent } from '../../modals/login/login.component'
import { ReportVendorComponent} from '../../modals/report-vendor/report-vendor.component'
import { EventEditComponent} from '../../modals/event-edit/event-edit.component'

@Component({
  selector: 'app-front-page',
  templateUrl: './front-page.component.html',
  styleUrls: ['./front-page.component.css']
})
export class FrontPageComponent implements OnInit {
  rc = RegisterComponent;
  lc = LoginComponent;
  reportVendorComponent = ReportVendorComponent;
  eventEditComponent = EventEditComponent;

  constructor(private modalService: NgbModal) { }

  ngOnInit() {
  }

  open(component: Component) {
    let modalReg = this.modalService.open(component);
  }

}
