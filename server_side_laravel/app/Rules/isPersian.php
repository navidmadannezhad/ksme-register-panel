<?php

namespace App\Rules;

use Illuminate\Contracts\Validation\Rule;

class isPersian implements Rule
{
    /**
     * Create a new rule instance.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }

    /**
     * Determine if the validation rule passes.
     *
     * @param  string  $attribute
     * @param  mixed  $value
     * @return bool
     */
    public function passes($attribute, $value)
    {
        if(!preg_match("/^[آ ا ب پ ت ث ج چ ح خ د ذ ر ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ه ی]/", $value)){
            return false;
        }else{
            if (preg_match('/[A-Za-z0-9]/', $value)){
                return false;
            }else{
                return true;
            }
        }
        return $value;
    }

    /**
     * Get the validation error message.
     *
     * @return string
     */
    public function message()
    {
        return 'لطفا :attribute خود را به فارسی وارد کنید';
    }
}
