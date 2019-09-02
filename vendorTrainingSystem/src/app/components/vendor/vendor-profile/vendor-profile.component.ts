import { Component, OnInit, Input } from '@angular/core';
import { Vendor } from 'src/app/models/Vendor';
import { EventEditComponent } from '../../../modals/event-edit/event-edit.component';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { HttpClient } from '@angular/common/http';
import { UserService } from 'src/app/user.service';
import { AboutComponent } from '../../../modals/about/about.component';
import { EditVendorProfileComponent } from '../../../modals/edit-vendor-profile/edit-vendor-profile.component';
import { ReportVendorComponent } from '../../../modals/report-vendor/report-vendor.component';

@Component({
  selector: 'app-vendor-profile',
  templateUrl: './vendor-profile.component.html',
  styleUrls: ['./vendor-profile.component.css']
})
export class VendorProfileComponent implements OnInit {

  vendor: Vendor;

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
  openEditVendorProfileModal(){
    let modalReg = this.modalService.open(EditVendorProfileComponent);
  }
  openReportVendorModal(){
    let modalReg = this.modalService.open(ReportVendorComponent);
  }
  openEventEditModal(){
    let modalReg = this.modalService.open(EventEditComponent);
  }
}
