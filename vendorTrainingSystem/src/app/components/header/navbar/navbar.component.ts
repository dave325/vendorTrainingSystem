import { LoggerService } from './../../../services/Logger.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  constructor(
    public logger: LoggerService
  ) { }

  ngOnInit() {
  }

}
