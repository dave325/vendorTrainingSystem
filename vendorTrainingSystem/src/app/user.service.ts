import { AuthenticationService } from './services/Authentication.service';
import { DeleteProfileComponent } from './modals/delete-profile/delete-profile.component';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpEvent } from '@angular/common/http';
import { User } from './models/User';

@Injectable({
  providedIn: 'root'
})
export class UserService {



  private readonly getUserRoute: string = "/getUser";
  private readonly setUserRoute: string = "/setUser";

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

  static getUser(): Promise<HttpEvent<User>> {
    // TODO hash information
    return JSON.parse(window.sessionStorage.getItem('user'));
  } 

  editProfile(user){
    return this.http.post('/api/vendor/editProfile', user, this.httpOptions).toPromise();
  }

  deleteProfile(id){
    return this.http.post('/api/vendor/deleteProfile', id, this.httpOptions).toPromise();
  }

  getProfile(id){
    return this.http.post('/api/vendor/getProfile/', id, this.httpOptions).toPromise();
  }

}
