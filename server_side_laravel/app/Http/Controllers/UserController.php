<?php

namespace App\Http\Controllers;
use App\Models\User;
use App\Models\UserVerify;
use Validator;
use Illuminate\Support\Facades\Mail;

use App\Rules\isNumber;
use App\Rules\isPersian;
use Illuminate\Http\Request;
use Illuminate\Support\Str;


class UserController extends Controller
{

    public function level1(Request $request){

        $level1_validation = $this->validateLevel1($request->all());
        if($level1_validation->fails()){
            return response()->json([
                $level1_validation->messages()
            ][0], 400);
        }else{
            return response()->json([
                'message' => 'success'
            ], 200);
        }
        
    }

    public function level2(Request $request){

        $level2_validation = $this->validateLevel2($request->all());
        if($level2_validation->fails()){
            return response()->json([
                $level2_validation->messages()
            ][0], 400);
        }else{
            return response()->json([
                'message' => 'success'
            ], 200);
        }
        
    }


    public function level3(Request $request){

        $level3_validation = $this->validateLevel3($request->all());
        if($level3_validation->fails()){
            return response()->json([
                $level3_validation->messages()
            ][0], 400);
        }else{
            try{

                $user = User::create([
                    'first_name' => $request['first_name'],
                    'last_name' => $request['last_name'],
                    'phone_number' => $request['phone_number'],
                    'national_number' => $request['national_number'],
                    'birthday' => $request['birthday'],
                    'email' => $request['email'],
                    'educational_field' => $request['educational_field'],
                    'educational_level' => $request['educational_level'],
                    'student_number' => $request['student_number'],
                    'corporate_field' => $request['corporate_field'],
                    'skills' => $request['skills'],
                    'activities' => $request['activities'],
                    'extra_words' => $request['extra_words'],
    
                ]);

                $token = Str::random(64);
  
                UserVerify::create([
                    'user_id' => $user->id, 
                    'token' => $token
                ]);

                $context = ['token' => $token, 'full_name' => $request['first_name'].' '.$request['last_name']];
        
                Mail::send('verification.emailTemplate', $context, function($message) use($request){
                    $message->to($request['email']);
                    $message->subject('احراز هویت انجمن علمی مهندسی مکانیک');
                });

            }catch (Exception $e){
                return response()->json([
                    'error' => 'مشکل در سرور'
                ], 400);
            }
            return response()->json([
                'message' => 'success'
            ], 200);
        }
        
    }










    public function validateLevel1($request){
        $rules = [
            'first_name' => ['required', new isPersian],
            'last_name' => ['required', new isPersian],
            'email' => ['required', 'email', 'unique:users'],
            'birthday' => ['required'],
            'national_number' => ['required', new isNumber],
            'phone_number' => ['required', new isNumber],
        ];

        $messages = [
            'first_name.required' => 'لطفا نام خود را وارد کنید',
            'first_name.isPersian' => 'لطفا نام خود را به فارسی وارد کنید',
            'last_name.required' => 'لطفا نام خانوادگی خود را وارد کنید',
            'last_name.isPersian' => 'لطفا نام خانوادگی خود را به فارسی وارد کنید',
            'email.required' => 'لطفا ایمیل خود را وارد کنید',
            'email.email' => 'لطفا ایمیل خود را صحیح وارد کنید',
            'email.unique' => 'ایمیل مورد نظر ثبت شده است',
            'birthday.required' => 'لطفا تاریخ تولد خود را وارد کنید',
            'national_number.required' => 'لطفا کد ملی خود را وارد کنید',
            'phone_number.required' => 'لطفا شماره تماس خود را وارد کنید'
        ];

        $validatorResults = Validator::make($request, $rules, $messages);
        return $validatorResults;
    }

    public function validateLevel2($request){
        $rules = [
            'educational_field' => ['required'],
            'educational_level' => ['required'],
            'student_number' => ['required', new isNumber],
        ];

        $messages = [
            'educational_field.required' => 'لطفا رشته تحصیلی خود را وارد کنید',
            'educational_level.required' => 'لطفا مقطع خود را وارد کنید',
            'educational_level.isPersian' => 'لطفا مقطع تحصیلی خود را به وارد کنید',
            'student_number.required' => 'لطفا شماره دانشجویی خود را وارد کنید',
            'student_number.isPersian' => 'لطفا نام خانوادگی خود را به فارسی وارد کنید',
        ];

        $validatorResults = Validator::make($request, $rules, $messages);
        return $validatorResults;
    }

    public function validateLevel3($request){
        $rules = [
            'corporate_field' => ['required'],
        ];

        $messages = [
            'corporate_field.required' => 'لطفا حوزه همکاری خود را مشخص کنید',
        ];

        $validatorResults = Validator::make($request, $rules, $messages);
        return $validatorResults;
    }
}
