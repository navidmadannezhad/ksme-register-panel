<?php

namespace App\Http\Controllers;

use App\Rules\isNumber;
use App\Rules\isPersian;
use Illuminate\Http\Request;

class UserController extends Controller
{
    public function level1(Request $request){

        $level1_validation = $this->validateLevel1($request->all());
        if($level1_validation->fails()){
            return response()->json([
                'errors' => $level1_validation->messages()
            ], 400);
        }else{
            return response()->json([
                'message' => 'success'
            ], 200);
        }
        
    }










    public function validateLevel1($request){
        $rules = [
            'first_name' => ['required', new isPersian],
            'last_name' => ['required', new isPersian],
            'email' => ['required', 'email', 'unique:users, email'],
            'birthday' => ['required'],
            'national_number' => ['required', new isNumber],
            'phone_number' => ['required', new isNumber],
        ];

        $messages = [
            'first_name.required' => 'لطفا نام خود را وارد کنید',
            'first_name.isPersian' => 'لطفا نام خود را به فارسی وارد کنید',
            'last_name.required' => 'لطفا نام خانوادگی خود را وارد کنید',
            'last_name.isPersian' => 'لطفا نام خانوادگی خود را به فارسی وارد کنید',
            'email.email' => 'لطفا ایمیل خود را صحیح وارد کنید',
            'email.unique' => 'ایمیل مورد نظر ثبت شده است',
            'birthday.required' => 'لطفا تاریخ تولد خود را وارد کنید',
            'national_number.required' => 'لطفا کد ملی خود را وارد کنید',
            'phone_number.required' => 'لطفا شماره تماس خود را وارد کنید'
        ];

        $validatorResults = Validator::make($request, $rules, $messages);
        return $validatorResults;
    }




    public function test(){
        return 'false';
    }
}
