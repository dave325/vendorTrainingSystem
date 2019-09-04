import { Component, OnInit, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'dsol-edit-vendor-profile',
  templateUrl: './edit-vendor-profile.component.html',
  styleUrls: ['./edit-vendor-profile.component.css']
})
export class EditVendorProfileComponent implements OnInit {

  @Input() vendor;
  constructor(
    private modal: NgbActiveModal
  ) { 
    console.log(this.vendor)
  }

  ngOnInit() {
  }


}
