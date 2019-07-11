import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-report-vendor',
  templateUrl: './report-vendor.component.html',
  styleUrls: ['./report-vendor.component.css']
})
export class ReportVendorComponent implements OnInit {
  vendorNameText: string;
  violationText: string;
  constructor() {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    let valid: boolean;
    alert("reported vendor: "+this.vendorNameText+", violation: "+this.violationText);
    
    
  }
}
