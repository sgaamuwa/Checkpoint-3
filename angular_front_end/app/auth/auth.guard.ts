import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable()
export class AuthGuard implements CanActivate{
    constructor(private _authService: AuthService, private _router: Router){

    }

    canActivate(): boolean {
        if(this._authService.isLoggedIn()){
            return this._authService.isLoggedIn();
        };
        this._router.navigate(['/auth']);
        return false;
    }
}

@Injectable()
export class LoginGuard implements CanActivate{
    constructor(private _authService: AuthService, private _router: Router){

    }

    canActivate(): boolean {
        if(!this._authService.isLoggedIn()){
            return true;
        };
        this._router.navigate(['/bucketlists']);
        return false;
    }
}