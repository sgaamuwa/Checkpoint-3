import { Component } from '@angular/core';
import { AuthService } from './auth.service';

@Component({
    selector: 'bl-auth',
    moduleId: module.id,
    templateUrl: "auth.component.html",
    providers: [AuthService]
})
export class AuthComponent {
    pageTitle: string = "Authentication";
    username: string;
    password: string;
    email: string;
    register: boolean = false;

    constructor(private _authService: AuthService){

    }

    loginUser(): void {
        this._authService.loginUser(this.username, this.password);
    }

    registerUser(): void {
        this._authService.registerUser(this.username, this.password);
    }

    onRegister(): void {
        this.register = true;
    }
}