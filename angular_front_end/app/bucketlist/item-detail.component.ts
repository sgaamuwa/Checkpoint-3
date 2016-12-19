import { Component, Input, Output, OnInit, EventEmitter } from '@angular/core';
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
    @Output() itemUpdate = new EventEmitter();
    edit: boolean = false;
    isDone: boolean;
    newItemName: string;
    errorMessage: string;

    constructor(private _bucketlistService: BucketlistService){

    }
    ngOnInit(): void {
        this.newItemName = this.item.name;
        this.isDone = this.item.done;
    }

    toggleEdit(): void {
        this.edit = !this.edit;
        this.newItemName = this.item.name;
    }

    updateItem(): void {
        if (this.newItemName != this.item.name){
            this._bucketlistService.updateBucketlistItem(this.newItemName ,this.bucketlistId, this.item.id)
            .subscribe(
                (result) => {},
                error => this.errorMessage = error,
                () => this.reloadBucketlist()
            );
        }
        else if(this.isDone != this.item.done){
            this._bucketlistService.updateBucketlistItemDone(this.isDone ,this.bucketlistId, this.item.id)
            .subscribe(
                (result) => {},
                error => this.errorMessage = error,
                () => this.reloadBucketlist()
            );
        }   
    }

    deleteItem(): void {
        this._bucketlistService.deleteBucketlistItem(this.bucketlistId, this.item.id)
            .subscribe(
                (result) => {},
                error => this.errorMessage = error,
                () => this.reloadBucketlist()
            )
    }

    reloadBucketlist(): void {
        this.itemUpdate.emit()
    }
}