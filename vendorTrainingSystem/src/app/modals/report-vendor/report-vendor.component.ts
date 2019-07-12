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
  showModal:boolean = false;
  constructor() {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    let valid: boolean;
    alert("reported vendor: "+this.reportVendorModel.vendorName+", violation: "+this.reportVendorModel.violation);
    
    
  }
}
