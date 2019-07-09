import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-report-vendor',
  templateUrl: './report-vendor.component.html',
  styleUrls: ['./report-vendor.component.css']
})
export class ReportVendorComponent implements OnInit {
  errors: {vendorName: String, violation:String};
  vendorName: String;
  violation: String;
  constructor() {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    let valid: Boolean;
    if(this.vendorName === ""){
      this.errors.vendorName = "Please enter the name of the vendor";
      valid = false;
    }
    if(this.violation === ""){
      this.errors.violation = "Please provide the description of violation";
      valid = false;
    }
    if(valid){
      //pass data to database
    }
    
    
    
  }
}
