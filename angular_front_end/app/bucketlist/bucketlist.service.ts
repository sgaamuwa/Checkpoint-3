import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Http, Response, Headers } from '@angular/http';

import { Bucketlist, Item } from './bucketlist';4

@Injectable()
export class BucketlistService {
    private actionUrl: string; 
    private headers: Headers;

    constructor(private _http: Http){
        this.actionUrl = "http://127.0.0.1:8000";
        this.headers.append('Content-Type', 'application/json');
        this.headers.append('Authorization', 'Token ' + this.getToken());
    }

    getBucketlists(): Observable<Bucketlist[]> {
        return;
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

    getToken(): string {
        return;
    }
}