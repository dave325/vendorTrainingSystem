import { AuthenticationService } from './Authentication.service';
import { User } from './../models/User';
import { HttpHeaders, HttpClient, HttpEvent } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
  })
  export class EventServie {

  
    private readonly httpOptions=<any>{
  
    }
  
    constructor(
      private http: HttpClient,
      private auth: AuthenticationService
      ) {
  
  
      const headers = new HttpHeaders(
        {
          Authorization: 'Bearer ' + this.auth.getToken()
        }
      );
  
      this.httpOptions.headers = headers;
  
    }
    editEvent(event){
        return this.http.post('/api/vendor/editMyEvents/', event, this.httpOptions).toPromise();
    }

    viewEvents(userId){
        return this.http.post('/api/vendors/editMyEvents/', userId. this.httpOptions).toPromise();
    }

    listEvents () {
      return this.http.get('/api/vendors/getAllEvents/').toPromise();
    }

    deleteEvents (id) {
      return this.http.delete('/api/vendor/event/', id).toPromise();
    }

    joinEvent(information){
      this.http.post('/api/user/joinEvent/', information, this.httpOptions).toPromise();
    }
  }