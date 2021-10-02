@extends('base')

@section('content')
@if(isset($user))
  <div class="users">
      <div class="user" style="{{ $user->is_email_verified == 1 ? 'border-right-color:rgb(15, 134, 15)' : '' }}">
        <p class="fullname"><span>نام و نام خانوادگی:</span><span>{{ $user->first_name }}</span> <span>{{ $user->last_name }}</span></p>
        <p class="student_number"><span>شماره دانشجویی:</span><span>{{ $user->student_number }}</span></p>
        <p class="educational_field"><span>رشته تحصیلی:</span><span>{{ $user->educational_field }}</span></p>
        <p class="educational_level"><span>مقطع تحصیلی:</span><span>{{ $user->educational_level }}</span></p>
        <p class="birthday"><span>تاریخ تولد:</span><span>{{ $user->birthday }}</span></p>
        <p class="skills"><span>توانایی ها:</span><span>{{ $user->skills }}</span></p>
        <p class="activities"><span>فعالیت های کاری و پژوهشی:</span><span>{{ $user->activities }}</span></p>
        <p class="email"><span>ایمیل:</span><span>{{ $user->email }}</span></p>
        <p class="corpotate_field"><span>حوزه های همکاری:</span><span>{{ $user->corpotate_field }}</span></p>
        <p class="national_number"><span>کد ملی:</span><span>{{ $user->national_number }}</span></p>
        <p class="extra_words"><span>حرف های دیگر:</span><span>{{ $user->extra_words }}</span></p>
      </div>
  </div>
@else
  <div class="message">
    کاربر مورد نظر یافت نشد
  </div>
@endif
@endsection