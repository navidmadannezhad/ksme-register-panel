@extends('base')

@section('content')
@if(isset($users))
  <div class="users">
    @foreach($users as $user)

      <div class="user" style="{{ $user->is_email_verified == 1 ? 'border-right-color:rgb(15, 134, 15)' : '' }}">
        <p class="fullname"><span>نام و نام خانوادگی:</span><span>{{ $user->first_name }}</span> <span>{{ $user->last_name }}</span></p>
        <p class="student_number"><span>شماره دانشجویی:</span><span>{{ $user->student_number }}</span></p>
        <p class="educational_field"><span>رشته تحصیلی:</span><span>{{ $user->educational_field }}</span></p>
        <p class="educational_level"><span>مقطع تحصیلی:</span><span>{{ $user->educational_level }}</span></p>
        <a href="{{ route('userDetail', ['id' => $user->id]) }}">اطلاعات بیشتر</a>
      </div>

    @endforeach
  </div>
@else
  <div class="message">
    هنوز کاربری وجود ندارد
  </div>
@endif
@endsection