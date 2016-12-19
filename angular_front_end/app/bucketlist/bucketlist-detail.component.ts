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
    updateBucketlistError: string;
    createItemError: string 
    newItem: string;
    edit: boolean = false;


    constructor (private _route: ActivatedRoute, private _bucketlistService: BucketlistService) {

    }

    ngOnInit(): void {
        this.getBucketlist();
    }

    toggleEdit(): void {
        this.edit = !this.edit;
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
            .subscribe((result) => {
                            this.updateBucketlistError = null;
                        },
                        error => this.updateBucketlistError = <any>error,
                        () => {
                            this.toggleEdit();
                            this.getBucketlist()});
    }

    createItem(bucketlistId: number): void {
        this._bucketlistService.createBucketlistItem(bucketlistId, this.newItem)
            .subscribe((result) => {
                            this.createItemError = null;
                            this.newItem = null;
                        },
                        error => this.createItemError = <any>error,
                        () => this.getBucketlist());
    }
}