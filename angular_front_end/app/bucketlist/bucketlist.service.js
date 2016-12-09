"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var Observable_1 = require('rxjs/Observable');
var http_1 = require('@angular/http');
require('rxjs/add/operator/catch');
require('rxjs/add/operator/do');
require('rxjs/add/operator/map');
4;
var BucketlistService = (function () {
    function BucketlistService(_http) {
        this._http = _http;
        this.token = window.localStorage.getItem('auth_token');
        this.actionUrl = "http://127.0.0.1:8000/";
        this.headers = new http_1.Headers();
        this.headers.append('Content-Type', 'application/json');
        this.headers.append('Authorization', 'Token ' + this.token);
    }
    BucketlistService.prototype.getBucketlists = function () {
        return this._http.get(this.actionUrl + "bucketlists/", { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (data) { return console.log('All: ' + JSON.stringify(data)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.getOneBucketlist = function (bucketlistId) {
        return this._http.get(this.actionUrl + "bucketlists/" + bucketlistId, { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (response) { return console.log('All: ' + JSON.stringify(response)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.updateBucketlist = function (name, bucketlistId) {
        return this._http.put(this.actionUrl + "bucketlists/" + bucketlistId, JSON.stringify({ name: name }), { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (response) { return console.log('All: ' + JSON.stringify(response)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.createBucketlist = function (name) {
        return this._http.post(this.actionUrl + "bucketlists/", JSON.stringify({ name: name }), { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (response) { return console.log('All: ' + JSON.stringify(response)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.deleteBucketlist = function (bucketlistId) {
        return this._http.delete(this.actionUrl + "bucketlists/" + bucketlistId, { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (response) { return console.log('All: ' + JSON.stringify(response)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.updateBucketlistItem = function (name, bucketlistId, itemId) {
        return this._http.put(this.actionUrl + "bucketlists/" + bucketlistId + "/items/" + itemId, JSON.stringify({ name: name }), { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (response) { return console.log('All: ' + JSON.stringify(response)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.createBucketlistItem = function (bucketlistId, name) {
        return this._http.post(this.actionUrl + "bucketlists/" + bucketlistId + "/items/", JSON.stringify({ name: name }), { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (response) { return console.log('All: ' + JSON.stringify(response)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.deleteBucketlistItem = function (bucketlistId, itemId) {
        return this._http.delete(this.actionUrl + "bucketlists/" + bucketlistId + "/items/" + itemId, { headers: this.headers })
            .map(function (response) { return response.json(); })
            .do(function (response) { return console.log('All: ' + JSON.stringify(response)); })
            .catch(this.handleError);
    };
    BucketlistService.prototype.handleError = function (error) {
        console.error(error);
        return Observable_1.Observable.throw(error.json().error || 'Server error');
    };
    BucketlistService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [http_1.Http])
    ], BucketlistService);
    return BucketlistService;
}());
exports.BucketlistService = BucketlistService;
//# sourceMappingURL=bucketlist.service.js.map