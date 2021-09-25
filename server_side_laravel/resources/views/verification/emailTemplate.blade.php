@extends('verification.base')

@section('title')
احراز هویت
@endsection

@section('content')
<div class="verification-message">
    <p>
        سلام {{ $full_name }}!
    </p>
    <p>
        جهت تایید هویت کاربری در انجمن علمی مهندسی مکانیک بر لینک زیر کلیک کن.
    </p>
    <form action="{{ route('userVerify', ['token' => $token]) }}">
        <input type="submit" value="تایید هویت کاربری">
    </form>
</div>
@endsection