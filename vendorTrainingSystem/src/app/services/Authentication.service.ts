import { User } from "./../models/User";
import { HttpHeaders, HttpClient, HttpEvent } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  S;
  private readonly httpOptions = <any>{};
  constructor(private http: HttpClient) {
    const headers = new HttpHeaders({
      Authorization: 'Bearer ' + this.getToken()
    });

    this.httpOptions.headers = headers;
  }

  private getUser(user): Promise<HttpEvent<User>> {
    return this.http
      .post<User>('/api/user/getUser/', user, this.httpOptions)
      .toPromise();
  }

  getToken() {
    return JSON.parse(window.sessionStorage.getItem('userToken'));
  }

  //the token is stored as a string because it has to be sent back in the http header as a string

  private setToken(token) {
    window.sessionStorage.setItem('userToken', JSON.stringify(token));
  }

  /**
   *
   * @param user
   *
   * TODO set token and only return true/false to user
   */
  login(user) {
    return this.http.post('/api/user/login/', user).toPromise();
  }

  register(user) {
    return this.http.post('/api/user/register/', user).toPromise();
  }
  editProfile(user){
    return this.http.post('/api/user/profileEdit/', user).toPromise();
    
  }
  deleteProfile(user){
    return this.http.post('/api/user/profileDelete/', user).toPromise();
  }
}
