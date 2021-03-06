import { User } from './../models/User';
import { HttpHeaders, HttpClient, HttpEvent } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthenticationService } from "./Authentication.service";

@Injectable({
    providedIn: 'root'
})
export class EventService {

  
    private readonly httpOptions=<any>{
  
    }
  
    constructor(
      private http: HttpClient,
      private auth: AuthenticationService
      ) {
      const headers = new HttpHeaders(
        {
          Authorization: 'Bearer ' + AuthenticationService.getToken()
        }
      );
  
      this.httpOptions.headers = headers;
  
    }
    //edit event not implemented
    editEvent(event){
        return this.http.post('/api/vendor/editMyEvents/', event, this.httpOptions).toPromise();
    }
    //view event not implemented
    viewEvents(userId){
        return this.http.post('/api/vendors/viewMyEvents/', userId, this.httpOptions).toPromise();
    }

    listEvents () {
      return this.http.get('/api/vendors/getAllEvents/').toPromise();
    }

    deleteEvents (id) {
      return this.http.delete('/api/vendor/event/', id).toPromise();
    }
    //join event incomplete
    joinEvent(information){
      this.http.post('/api/user/joinEvent/', information, this.httpOptions).toPromise();
    }
  }