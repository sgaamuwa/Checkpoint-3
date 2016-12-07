import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BucketlistService } from './bucketlist.service';
import { Bucketlist } from './bucketlist';

@Component({
    moduleId: module.id,
    templateUrl: 'bucketlist.component.html',
    styleUrls: [],
    providers:[BucketlistService]
})
export class BucketlistComponent implements OnInit {
    pageTitle: string = "Bucketlists"
    bucketlists: Bucketlist[];
    errorMessage: string;
    showDelete: boolean = false;
    showItems: boolean = false;
    newBucketlist: string;

    constructor(private _bucketlistService: BucketlistService, private _router: Router){

    }

    ngOnInit(): void {
        this._bucketlistService.getBucketlists()
            .subscribe(bucketlists => this.bucketlists = bucketlists,
                        error => this.errorMessage = <any>error);
    }

    toggleShowItems(): void {
        this.showItems = !this.showItems;
    }

    createBucketlist(): void {
        this._bucketlistService.createBucketlist(this.newBucketlist).subscribe(
            (result) => {
                if (result){
                    this._router.navigate(['/bucketlists'])
                }
            },
            error => this.errorMessage = <any>error);
    }

    deleteBucketlist(bucketlistId: number): void {
        this._bucketlistService.deleteBucketlist(bucketlistId).subscribe(
            (result) => {},
            error => this.errorMessage = <any>error);
    }
    
}