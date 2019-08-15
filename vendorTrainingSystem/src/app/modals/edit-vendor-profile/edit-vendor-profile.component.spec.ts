import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditVendorProfileComponent } from './edit-vendor-profile.component';

describe('EditVendorProfileComponent', () => {
  let component: EditVendorProfileComponent;
  let fixture: ComponentFixture<EditVendorProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EditVendorProfileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditVendorProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
