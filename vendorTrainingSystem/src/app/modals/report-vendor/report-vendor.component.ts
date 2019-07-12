import { Component, OnInit, Input } from '@angular/core';
import {NgbActiveModal} from '@ng-bootstrap/ng-bootstrap';

interface ReportVendorModel{
  vendorName: string;
  violation: string;
}

@Component({
  selector: 'dsol-report-vendor',
  templateUrl: './report-vendor.component.html',
  styleUrls: ['./report-vendor.component.css']
})
export class ReportVendorComponent implements OnInit {
  reportVendorModel = <ReportVendorModel>{};
  
  constructor(activeModal: NgbActiveModal) {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    let valid: boolean;
    alert("reported vendor: "+this.reportVendorModel.vendorName+", violation: "+this.reportVendorModel.violation);
    
    
  }
}
