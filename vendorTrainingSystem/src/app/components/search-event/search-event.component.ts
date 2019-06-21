import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-search-event',
  templateUrl: './search-event.component.html',
  styleUrls: ['./search-event.component.css']
})
export class SearchEventComponent implements OnInit {

  searchTerm:string;

  constructor() { }

  ngOnInit() {
  }

  onSubmit():void{
    const searchTerm = this.searchTerm;
    console.log(searchTerm);
  }

}
