import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-report-vendor',
  templateUrl: './report-vendor.component.html',
  styleUrls: ['./report-vendor.component.css']
})
export class ReportVendorComponent implements OnInit {
  vendorText: String;
  
  constructor() {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    let valid: Boolean;
    alert(this.vendorText);
    
    
  }
}
