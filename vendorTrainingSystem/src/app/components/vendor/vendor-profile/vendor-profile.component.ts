import { Component, OnInit, Input } from '@angular/core';
import { Vendor } from 'src/app/models/Vendor';
import { EventEditComponent } from '../../../modals/event-edit/event-edit.component'
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http';
import { UserService } from 'src/app/user.service';
import { AboutComponent } from '../../../modals/about/about.component'

@Component({
  selector: 'app-vendor-profile',
  templateUrl: './vendor-profile.component.html',
  styleUrls: ['./vendor-profile.component.css']
})
export class VendorProfileComponent implements OnInit {

  @Input() vendor: Vendor;

  constructor(
    private modalService: NgbModal,
    private http: HttpClient,
    private userService: UserService,
  ) {
  }

  ngOnInit() {
  }

  openAboutModal() {
    let modalReg = this.modalService.open(AboutComponent);
  }

}
