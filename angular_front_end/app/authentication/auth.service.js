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
var core_1 = require("@angular/core");
var http_1 = require("@angular/http");
var AuthService = (function () {
    function AuthService(_http) {
        this._http = _http;
        this.actionUrl = "http://127.0.0.1:8000/api/auth/";
        this.headers.append('Content-Type', 'application/json');
    }
    AuthService.prototype.loginUser = function (username, password) {
        this._http.post((this.actionUrl + "login/"), JSON.stringify({ username: username, password: password }), { headers: this.headers })
            .subscribe(function (data) {
            if (data.json().auth_token) {
                window.localStorage.setItem('auth_token', data.json().auth_token);
            }
        });
    };
    AuthService.prototype.registerUser = function (username, password) {
        return this._http.post((this.actionUrl + "register/"), JSON.stringify({ username: username, password: password }), { headers: this.headers })
            .subscribe(function (data) { data.json().username; });
    };
    AuthService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [http_1.Http])
    ], AuthService);
    return AuthService;
}());
exports.AuthService = AuthService;
//# sourceMappingURL=auth.service.js.map