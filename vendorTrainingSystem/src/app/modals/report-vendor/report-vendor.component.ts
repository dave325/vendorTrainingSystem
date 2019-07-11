import { Component, OnInit } from '@angular/core';

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
  constructor() {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    let valid: Boolean;
    alert("reported vendor: "+this.reportVendorModel.vendorName+", violation: "+this.reportVendorModel.violation);
    
    
  }
}
