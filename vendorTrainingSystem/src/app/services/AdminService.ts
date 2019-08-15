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
      Authorization: "Bearer " + this.auth.getToken()
    });

    this.httpOptions.headers = headers;
  }

  getAllCustomers() {
    return this.http.post("/api/admin/listCustomers/", {}, this.httpOptions);
  }

  getAllVendors() {
    return this.http.post("/api/admin/listVendors/", {}, this.httpOptions);
  }

  approveVendor() {
    return this.http.post("/api/admin/approveVendor/", {}, this.httpOptions);
  }

  disproveVendor() {
    return this.http.post("/api/admin/disproveVendor/", {}, this.httpOptions);
  }

  viewCustomer() {
    return this.http.post("/api/admin/viewCustomer/", {}, this.httpOptions);
  }
}
