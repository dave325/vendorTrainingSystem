import { Component, OnInit, Input } from '@angular/core';
import {NgbActiveModal} from '@ng-bootstrap/ng-bootstrap';
import {UserService} from '../../user.service';
import { User } from 'src/app/models/User';
import { Vendor} from '../../models/Vendor';
interface ReportVendorModel{
  vendorName: string;
  violation: string;
}

@Component({
  selector: 'dsol-report-vendor',
  templateUrl: './report-vendor.component.html',
  styleUrls: ['./report-vendor.component.css']
})
export class ReportVendorComponent implements OnInit {
  reportVendorModel = <ReportVendorModel>{};
  vendor= {
    name: 'name', address: 'address', phone: 'phone', email: 'email', is_approved: false
  }
  info = null;
  error = null;
  constructor(activeModal: NgbActiveModal,
    private userService: UserService
    ) {
    
  }

  ngOnInit() {
  }

  onSubmitReport(){
    UserService.getUser().then(
      (res) =>{
        
      },
      (err)=>{

      }
    )
    let valid: boolean;
    alert("reported vendor: "+this.reportVendorModel.vendorName+", violation: "+this.reportVendorModel.violation);
    
    
  }
}
