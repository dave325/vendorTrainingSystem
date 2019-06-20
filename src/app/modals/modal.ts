export interface modal {
  isDisable:boolean;
  submit(url:string, data:any);
  cancel(url:string, data:any);
  reset(url:string, data:any);
}