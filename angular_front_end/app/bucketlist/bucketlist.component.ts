import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BucketlistService } from './bucketlist.service';
import { Bucketlist } from './bucketlist';

@Component({
    moduleId: module.id,
    templateUrl: 'bucketlist.component.html',
    styleUrls: ['bucketlist.component.css'],
    providers:[BucketlistService]
})
export class BucketlistComponent implements OnInit {
    pageTitle: string = "Bucketlists";
    bucketlists: Bucketlist[];
    count: number;
    nextPage: string;
    previousPage: string;
    errorMessage: string;
    showItems: boolean = false;
    newBucketlist: string;

    constructor(private _bucketlistService: BucketlistService, private _router: Router){

    }

    ngOnInit(): void {
        this.getBucketlists();
    }

    getBucketlists(): void {
        this._bucketlistService.getBucketlists()
            .subscribe(bucketlists => {
                this.bucketlists = bucketlists.results;
                this.count = bucketlists.count;
                this.nextPage = bucketlists.next;
                this.previousPage = bucketlists.previous;
                },
                error => this.errorMessage = <any>error);
    }

    createBucketlist(): void {
        this._bucketlistService.createBucketlist(this.newBucketlist).subscribe(
            (result) => {},
            error => this.errorMessage = <any>error,
            () => this.getBucketlists());
    }

    deleteBucketlist(bucketlistId: number): void {
        this._bucketlistService.deleteBucketlist(bucketlistId).subscribe(
            (result) => {},
            error => this.errorMessage = <any>error,
            () => this.getBucketlists());
    }
    
}