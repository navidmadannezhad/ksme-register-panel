@extends('verification.base')

@section('title')
احراز هویت
@endsection

@section('content')
<div class="success">
    <p>
        سلام {{ $full_name }}!
    </p>
    <p>
        جهت تایید هویت کاربری بر لینک زیر کلیک کن.
    </p>
    <form action="{{ route('userVerify', ['token' => $token]) }}">
        <input type="submit" value="تایید هویت کاربری">
    </form>
</div>
@endsection