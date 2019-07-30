import { Component, OnInit } from '@angular/core';
import { Vendor } from '../../models/Vendor';
import { dummy_vendors } from '../../dummy-data/dummy-vendors';

@Component({
  selector: 'app-vendor',
  templateUrl: './vendor.component.html',
  styleUrls: ['./vendor.component.css']
})
export class VendorComponent implements OnInit {

  Vendors:Vendor[] = dummy_vendors;

  constructor() {
    
   }

  ngOnInit() {
  }

}
