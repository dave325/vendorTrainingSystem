import { Injectable } from "@angular/core";

@Injectable()
export class LoggerService {
    private msg;
    private status = ['error','success','info'];
    constructor(){ }

    getMsg(){
        return this.msg;
    }

    setMsg(message){
        this.msg = message;
    }

    setStatus(status){
        this.status = status;
    }

    getStatus(){
        return this.status;
    }
}