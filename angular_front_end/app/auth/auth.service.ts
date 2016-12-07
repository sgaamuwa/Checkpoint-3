import { Injectable } from "@angular/core";
import { Http, Headers } from "@angular/http";

@Injectable()
export class AuthService {

    private actionUrl: string;
    private headers: Headers;

    constructor (private _http: Http){
        this.actionUrl = "http://127.0.0.1:8000/auth/";
        this.headers = new Headers();
        this.headers.append('Content-Type', 'application/json');
    }

    loginUser(username: string, password: string){
       this._http.post(
            (this.actionUrl+"login/"),
            JSON.stringify({ username, password }),
            {headers: this.headers})
            .subscribe((data) => {
                if(data.json().auth_token) {
                    window.localStorage.setItem('auth_token', data.json().auth_token);
                }
            });
    }

    registerUser(username: string, password: string){
        return this._http.post(
            (this.actionUrl+"register/"),
            JSON.stringify({ username, password }),
            {headers: this.headers})
            .subscribe((data) => {data.json().username});
    }
}