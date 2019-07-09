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

  constructor(private http: HttpClient) {


    let headers = new HttpHeaders(
      {
        'Authorization': 'Bearer ' + this.getToken()
      }
    );

    this.httpOptions.headers = headers;

  }

  getUser(): Promise<HttpEvent<User>> {

    return this.http.post<User>(this.getUserRoute, {}, this.httpOptions).toPromise();
  } 

  public getToken() {
    return JSON.parse(window.sessionStorage.getItem('userToken'));
  }


  //the token is stored as a string because it has to be sent back in the http header as a string

  private setToken(token) {
    window.sessionStorage.setItem('userToken', JSON.stringify(token));
  }
}
