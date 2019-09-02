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
      Authorization: 'Bearer ' + AuthenticationService.getToken()
    });

    this.httpOptions.headers = headers;
  }


  private setUser(user) {
    window.sessionStorage.setItem('user', JSON.stringify(user));
  }
  

  public static getToken() {
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
    return new Promise((resolve, reject) => {
      this.http.post('/api/auth/login/', user).toPromise().then(
        (res: { success:Boolean, user: Object, token: {token:String}, error_message: string} ) => {
          console.log(res);
          if (res.success ) {
            this.setUser(res.user);
            this.setToken(res.token.token);
            resolve({ 'success': true })
          }else{
            reject(res.error_message)
          }
        },
        (err) => {
          reject(err.error_message);
        }
      )
    });
  }

  register(user) {
    return this.http.post('/api/auth/register/', user).toPromise();
  }
  editProfile(user) {
    return this.http.post('/api/user/profileEdit/', user).toPromise();

  }
  deleteProfile(user) {
    return this.http.post('/api/user/profileDelete/', user).toPromise();
  }
}
