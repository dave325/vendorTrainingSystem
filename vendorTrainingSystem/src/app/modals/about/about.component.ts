import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'dsol-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {
  vendorName: string;
  vendorAbout: string;
  vendorContact: string;

  constructor() { }

  ngOnInit() {
  }

}