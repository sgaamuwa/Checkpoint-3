import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Http, Response, Headers } from '@angular/http';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/map';

import { Bucketlist, Item } from './bucketlist';4

@Injectable()
export class BucketlistService {
    private actionUrl: string; 
    private headers: Headers;
    private token = window.localStorage.getItem('auth_token');

    constructor(private _http: Http){
        this.actionUrl = "http://127.0.0.1:8000/";
        this.headers = new Headers();
        this.headers.append('Content-Type', 'application/json');
        this.headers.append('Authorization', 'Token ' + this.token);
    }

    getBucketlists(): Observable<Bucketlist[]> {
        return this._http.get(this.actionUrl+"bucketlists/", {headers: this.headers})
            .map((response: Response) => <Bucketlist[]>response.json())
            .do(data => console.log('All: ' + JSON.stringify(data)))
            .catch(this.handleError);
    }

    getOneBucketlist(): Observable<Bucketlist>{
        return;
    }

    updateBucketlist(): Observable<Bucketlist>{
        return;
    }

    createBucketlist(): Observable<Bucketlist>{
        return;
    }

    deleteBucketlist(): void {

    }

    updateBucketlistItem(): Observable<Item>{
        return;
    }

    createBucketlistItem(): Observable<Item>{
        return;
    }

    deleteBucketlistItem(): void {
        
    }

    private handleError(error: Response){
        console.error(error);
        return Observable.throw(error.json().error || 'Server error');
    }
}