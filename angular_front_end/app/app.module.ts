import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent }  from './app.component';
import { AuthComponent } from './auth/auth.component';
import { AuthGuard } from './auth/auth.guard';
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
      { path: 'auth', component: AuthComponent },
      { path: 'bucketlists', component: BucketlistComponent, canActivate: [AuthGuard] },
      { path: 'bucketlists/:id', component: BucketlistDetailComponent, canActivate: [AuthGuard] },
      { path: '', redirectTo: 'auth', pathMatch: 'full' },
      { path: '**', redirectTo: 'welcome', pathMatch: 'full'}
    ]) 
  ],
  declarations: [ 
    AppComponent,
    AuthComponent,
    BucketlistComponent,
    BucketlistDetailComponent,
    ItemDetailComponent 
  ],
  providers: [ AuthGuard, AuthService ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }