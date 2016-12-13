import { Component } from '@angular/core';
import { AuthService } from './auth/auth.service';


@Component({
	selector: 'my-app',
	moduleId: module.id,
	templateUrl: "app.component.html",
	styleUrls: ["app.component.css"]
})

export class AppComponent{
	public description: string = "Ebyokola"

	constructor(private _authService: AuthService){

	}

	logoutUser(): void {
		this._authService.logoutUser();
	}
}