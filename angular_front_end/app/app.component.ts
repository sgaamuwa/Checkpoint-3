import { Component } from '@angular/core';

@Component({
	selector: 'my-app',
	template: `<h3 class="jumbotron text-center"> 
	                Hello World, Welcome to {{description}}
	          </h3>
	          `
})

export class AppComponent{
	public description: string = 'Angular 2 Boilerplate'

}