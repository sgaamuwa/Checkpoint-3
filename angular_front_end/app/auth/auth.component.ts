import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
    selector: 'bl-auth',
    moduleId: module.id,
    templateUrl: "auth.component.html",
    styleUrls: ["auth.component.css"],
})
export class AuthComponent {
    pageTitle: string = "Authentication";
    username: string;
    password: string;
    confirmPassword: string;
    email: string;
    login: boolean = true;
    welcomeMessage: string;
    errorMessage: string;

    constructor(private _authService: AuthService, private _router: Router){

    }

    loginUser(): void {
        this._authService.loginUser(this.username, this.password).subscribe(
            (result) => {
                if (result){
                    this._router.navigate(['/bucketlists']);
                };
            },
            error => this.errorMessage = <any>error);
    }

    registerUser(): void {
        this._authService.registerUser(this.username, this.password).subscribe(
            (result) => {
                if (result){
                    this.welcomeMessage = "Welcome " + result + "!, Login to continue";
                    this.login = true; 
                    this.username = null;
                    this.password = null;
                    this._router.navigate(['/auth']);
                };
            },
            error => this.errorMessage = <any>error);
    }

    onRegister(): void {
        this.login = false;
        this.resetValues();
    }

    onLogin(): void{
        this.login = true;
        this.resetValues();
    }

    resetValues(): void {
        this.username = null;
        this.password = null;
        this.confirmPassword = null;
        this.email = null;
        this.errorMessage = null;
        this.welcomeMessage = null;
    }
}