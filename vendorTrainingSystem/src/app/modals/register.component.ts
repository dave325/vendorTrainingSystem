import { Component } from '@angular/core';

@Component({
    selector: 'app-register',
    templateUrl: './register.component.html',
    styleUrls: ['./register.component.css']
})

export class RegisterComponent {

    //these two lines are temporary 
    submitted = false;

    ngSubmit() { this.submitted = true; }

}


 // WILL DO - KARANVIR