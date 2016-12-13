import { Injectable } from "@angular/core";
import { Http, Headers } from "@angular/http";
import { Router } from "@angular/router";
import 'rxjs/add/operator/map';

@Injectable()
export class AuthService {

    private actionUrl: string;
    private headers: Headers;
    private loggedIn: boolean = false;

    constructor (private _http: Http, private _router: Router){
        this.actionUrl = "http://127.0.0.1:8000/auth/";
        this.headers = new Headers();
        this.headers.append('Content-Type', 'application/json');
        this.loggedIn = !!window.localStorage.getItem('auth_token');
    }

    loginUser(username: string, password: string){
       return this._http.post(
            (this.actionUrl+"login/"),
            JSON.stringify({ username, password }),
            {headers: this.headers})
            .map((res) => {
                if(res.json().auth_token) {
                    window.localStorage.setItem('auth_token', res.json().auth_token);
                    this.loggedIn = true;
                    return res.json().auth_token;
                }
            });
    }

    registerUser(username: string, password: string){
        return this._http.post(
            (this.actionUrl+"register/"),
            JSON.stringify({ username, password }),
            {headers: this.headers})
            .map((res) => {
                return res.json().username;
            });
    }

    logoutUser(){
        window.localStorage.removeItem('auth_token');
        this.loggedIn = false;
        this._router.navigate(['/auth']);
    }

    isLoggedIn(): boolean {
        return this.loggedIn;
    }
}