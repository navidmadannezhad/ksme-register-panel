@extends('verification.base')

@section('title')
عملیات ناموفق
@endsection

@section('content')
<div class="error">
    <p>
        {{ $message }}
    </p>
</div>
@endsection