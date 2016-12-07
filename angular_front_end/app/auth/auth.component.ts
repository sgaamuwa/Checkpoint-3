import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
    selector: 'bl-auth',
    moduleId: module.id,
    templateUrl: "auth.component.html",
    styleUrls: ["auth.component.css"],
    providers: [AuthService]
})
export class AuthComponent {
    pageTitle: string = "Authentication";
    username: string;
    password: string;
    email: string;
    login: boolean = true;
    welcomeMessage: string;

    constructor(private _authService: AuthService, private _router: Router){

    }

    loginUser(): void {
        this._authService.loginUser(this.username, this.password).subscribe(
            (result) => {
                if (result){
                    this._router.navigate(['/bucketlists']);
                };
            });
    }

    registerUser(): void {
        this._authService.registerUser(this.username, this.password).subscribe(
            (result) => {
                if (result){
                    this.welcomeMessage = "Welcome " + result + "!, Login to continue";
                    this.login = true; 
                    this._router.navigate(['/auth']);
                };
            });
    }

    onRegister(): void {
        this.login = false;
    }

    onLogin(): void{
        this.login = true;
    }
}