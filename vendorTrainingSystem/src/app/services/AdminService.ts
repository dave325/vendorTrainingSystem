import { AuthenticationService } from "./Authentication.service";
import { User } from "./../models/User";
import { HttpHeaders, HttpClient, HttpEvent } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({
  providedIn: "root"
})
export class AdminService {
  private readonly httpOptions = <any>{};

  constructor(private http: HttpClient, private auth: AuthenticationService) {
    const headers = new HttpHeaders({
      Authorization: "Bearer " + AuthenticationService.getToken()
    });

    this.httpOptions.headers = headers;
  }

  getAllCustomers() {
    return this.http.get("/api/admin/listCustomers/", this.httpOptions).toPromise();
  }

  getAllVendors() {
    return this.http.get("/api/admin/listVendors/", this.httpOptions).toPromise();
  }

  approveVendor(vendor) {
    return this.http.post("/api/admin/approveVendor/", vendor, this.httpOptions).toPromise();
  }

  disproveVendor(vendor) {
    return this.http.post("/api/admin/disproveVendor/", vendor, this.httpOptions).toPromise();
  }

  viewCustomer(customer) {
    return this.http.post("/api/admin/viewCustomer/", customer, this.httpOptions).toPromise();
  }

}
