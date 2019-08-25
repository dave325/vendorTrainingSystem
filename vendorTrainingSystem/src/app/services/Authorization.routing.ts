import { LoggerService } from './Logger.service';
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
    private pages = [];
    constructor(
        private http: HttpClient,
        private router: Router,
        private authentication: AuthenticationService,
        private logger: LoggerService
    ) {
        const headers = new HttpHeaders({
            Authorization: 'Bearer ' + AuthenticationService.getToken()
        });

        this.httpOptions.headers = headers;
    }

    /**
     * 
     * @param route 
     * @param state 
     * 
     * Checks authorization for specific routes
     */
    canActivate(
        route: ActivatedRouteSnapshot,
        state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
        
        let url: string = state.url;
        if( route.url[0] && route.url[0].path.length == 0){
            return false;
        }

        let path = route.url[0].path;
        //guard makes routes accesibly only server responds with a valid token
        return this.verifyToken(UserService.getUser()).then(
            (res: any) => {
                console.log(res)
                if (res.success) {
                    return this.checkLogin(res.role_info,path,route)
                }
                else {
                    this.logger.setMsg(null);
                    this.logger.setStatus('primary');
                    this.router.navigate(
                        [
                            ''
                        ]
                    );
                    return false;
                }
            },
            (err) => {
                console.log(err.error.Error)
                this.logger.setMsg(err.error.Error);
                this.logger.setStatus('danger');
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

    /**
     * 
     * @param role 
     * @param path 
     * @param route
     * 
     * Checks the status of user login against role information returned from db 
     */
    checkLogin(role: number, path: string, route: ActivatedRouteSnapshot) {
        console.log(role)
        switch (role) {
            case 0:
                if (path == "customer") {
                    this.logger.setMsg(null);
                    this.logger.setStatus(null);
                    return true;
                } else {
                    this.logger.setMsg("Invalid User");
                    this.logger.setStatus('warning');
                    this.router.navigate(['/']);
                    return false;
                }
            case 1:
                if (path == "vendor") {
                    this.logger.setMsg(null);
                    this.logger.setStatus(null);
                    return true;
                } else {
                    this.logger.setMsg("Invalid User");
                    this.logger.setStatus('warning');
                    this.router.navigate(['/']);
                    return false;
                }
            case 2:
                if (path == "admin") {
                    this.logger.setMsg(null);
                    this.logger.setStatus(null);
                    return true;
                } else {
                    this.router.navigate(['/']);
                    return false;
                }
            default:
                this.logger.setMsg("Invalid User");
                this.logger.setStatus('warning');
                this.router.navigate(['/']);
                return false;
        }
    }
}