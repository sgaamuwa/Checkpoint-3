import { Component, Input, OnInit } from '@angular/core';
import { Bucketlist, Item } from './bucketlist';
import { BucketlistService } from './bucketlist.service';

@Component({
    selector: 'bl-itemDetail',
    moduleId: module.id, 
    templateUrl: 'item-detail.component.html'
})
export class ItemDetailComponent implements OnInit{
    @Input() item: Item;
    @Input() bucketlistId: number;
    edit: boolean = false;
    newItemName: string;
    errorMessage: string;

    constructor(private _bucketlistService: BucketlistService){

    }
    ngOnInit(): void {
        this.newItemName = this.item.name;
    }

    toggleEdit(): void {
        this.edit = !this.edit;
        this.newItemName = this.item.name;
    }

    updateItem(): void {
        this._bucketlistService.updateBucketlistItem(this.newItemName ,this.bucketlistId, this.item.id)
            .subscribe(
                (result) => {},
                error => this.errorMessage = error
            );
    }
}