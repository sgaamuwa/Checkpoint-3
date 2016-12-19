import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent }  from './app.component';
import { AuthComponent } from './auth/auth.component';
import { AuthGuard, LoginGuard } from './auth/auth.guard';
import { AuthService } from './auth/auth.service';
import { BucketlistComponent } from './bucketlist/bucketlist.component';
import { BucketlistDetailComponent } from './bucketlist/bucketlist-detail.component';
import { ItemDetailComponent } from './bucketlist/item-detail.component';

@NgModule({
  imports: [ 
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
      { path: 'auth', component: AuthComponent, canActivate: [LoginGuard] },
      { path: 'bucketlists', component: BucketlistComponent, canActivate: [AuthGuard] },
      { path: 'bucketlists/:id', component: BucketlistDetailComponent, canActivate: [AuthGuard] },
      { path: '', redirectTo: 'bucketlists', pathMatch: 'full' },
      { path: '**', redirectTo: 'bucketlists', pathMatch: 'full'}
    ]) 
  ],
  declarations: [ 
    AppComponent,
    AuthComponent,
    BucketlistComponent,
    BucketlistDetailComponent,
    ItemDetailComponent 
  ],
  providers: [ AuthGuard, AuthService, LoginGuard ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }