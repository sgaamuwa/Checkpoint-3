import { Component, OnInit } from '@angular/core';
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

    constructor(private _bucketlistService: BucketlistService){

    }

    ngOnInit(): void {
        this._bucketlistService.getBucketlists()
            .subscribe(bucketlists => this.bucketlists = bucketlists,
                        error => this.errorMessage = <any>error);
    }
}