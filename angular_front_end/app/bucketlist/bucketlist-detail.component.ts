import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Bucketlist, Item } from './bucketlist';
import { BucketlistService } from './bucketlist.service';

@Component({
    moduleId: module.id,
    templateUrl: 'bucketlist-detail.component.html',
    styleUrls: ['bucketlist-detail.component.css'],
    providers: [BucketlistService]
})
export class BucketlistDetailComponent implements OnInit {
    pageTitle: string = "Bucketlist Details";
    bucketlist: Bucketlist;
    bucketlistName: string;
    item : Item[];
    errorMessage: string;
    newItem: string;


    constructor (private _route: ActivatedRoute, private _bucketlistService: BucketlistService) {

    }

    ngOnInit(): void {
        this.getBucketlist();
    }

    getBucketlist(): void{
        let id = +this._route.snapshot.params['id'];
        this._bucketlistService.getOneBucketlist(id).subscribe(
            bucketlist =>{
                this.bucketlist = bucketlist;
                this.bucketlistName = bucketlist.name}, 
            error => this.errorMessage = <any>error);
    }

    updateBucketlist(bucketlistId: number): void {
        this._bucketlistService.updateBucketlist(this.bucketlistName, bucketlistId)
            .subscribe((result) => {},
                        error => this.errorMessage = <any>error,
                        () => this.getBucketlist());
    }

    createItem(bucketlistId: number): void {
        this._bucketlistService.createBucketlistItem(bucketlistId, this.newItem)
            .subscribe((result) => {},
                        error => this.errorMessage = <any>error,
                        () => this.getBucketlist());
    }

    deleteItem(bucketlistId: number, itemId: number): void {
        this._bucketlistService.deleteBucketlistItem(bucketlistId, itemId)
            .subscribe((result) => {},
                        error => this.errorMessage = <any>error);
    }
}