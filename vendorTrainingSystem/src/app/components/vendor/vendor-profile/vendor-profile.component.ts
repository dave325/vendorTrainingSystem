import { Component, OnInit, Input } from '@angular/core';
import { Vendor } from 'src/app/models/Vendor';

@Component({
  selector: 'app-vendor-profile',
  templateUrl: './vendor-profile.component.html',
  styleUrls: ['./vendor-profile.component.css']
})
export class VendorProfileComponent implements OnInit {

  @Input() vendor:Vendor; 

  constructor() { 
  }

  ngOnInit() {
  }

  
}
