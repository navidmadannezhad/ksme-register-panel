<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Auth::routes(['verify' => true]);

Route::get('/admin', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

Route::get('/admin/{id}', [App\Http\Controllers\HomeController::class, 'userDetails'])->name('userDetail');

// email verification route
Route::get('account/verify/{token}', 'TokenController@verifyAccount')->name('userVerify'); 
