<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\UserVerify;

class TokenController extends Controller
{
    public function verifyAccount($token)
    {
        $verifyUser = UserVerify::where('token', $token)->first();
  
        $message = 'ایمیل شما در سیستم یافت نشد';
  
        if(!is_null($verifyUser) ){
            $user = $verifyUser->user;
              
            if(!$user->is_email_verified) {
                $verifyUser->user->is_email_verified = 1;
                $verifyUser->user->save();
                $message = "احراز هویت شما انجام شد. لطفا جهت ادامه فرآیند، از طریق کانال انجمن با ما در ارتباط باشید";
                return view('verification.success')->with('message', $message);
            } else {
                $message = "ایمیل شما قبلا تایید شده است. لطفا جهت ادامه فرآیند، از طریق کانال انجمن با ما در تماس باشید";
                return view('verification.success')->with('message', $message);
            }
        }
  
        return view('verification.error')->with('message', $message);
    }
}
