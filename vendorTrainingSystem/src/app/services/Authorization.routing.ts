import { UserService } from 'src/app/user.service';
import { AuthenticationService } from './Authentication.service';
import { HttpHeaders, HttpClient, HttpEvent } from "@angular/common/http";
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Injectable } from "@angular/core";
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class AuthorizationService implements CanActivate {
    private readonly httpOptions = <any>{};
    constructor(
        private http: HttpClient,
        private router: Router,
        private authentication: AuthenticationService) {
        const headers = new HttpHeaders({
            Authorization: 'Bearer ' + AuthenticationService.getToken()
        });

        this.httpOptions.headers = headers;
    }
    canActivate(
        next: ActivatedRouteSnapshot,
        state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {


        //guard makes routes accesibly only server responds with a valid token
        return this.verifyToken(UserService.getUser()).then(
            (res: any) => {
                console.log(res)
                if (res.success) {
                    return true;
                }
                else {
                    this.router.navigate(
                        [
                            ''
                        ]
                    );
                    return false;
                }
            },
            (err) => {
                console.log(err)
                this.router.navigate(
                    [
                        ''
                    ]
                );
                return false;
            }

        );
    }

    verifyToken(user) {
        return this.http.post('/api/auth/verifyToken/', user, this.httpOptions).toPromise();
      }
}