<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('api/test', 'UserController@test');

Route::group(['prefix' => 'api'], function(){
    Route::post('level1', 'UserController@level1');
    Route::post('level2', 'UserController@level2');
    Route::post('level3', 'UserController@level3');
    Route::get('activate/{uidb64}/{token}', 'UserController@activate');
});