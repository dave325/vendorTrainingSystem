import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-report-vendor',
  templateUrl: './report-vendor.component.html',
  styleUrls: ['./report-vendor.component.css']
})
export class ReportVendorComponent implements OnInit {
  vendorNameText: String;
  violationText: String;
  constructor() {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    let valid: Boolean;
    alert("reported vendor: "+this.vendorNameText+", violation: "+this.violationText);
    
    
  }
}
