@extends('verification.base')

@section('title')
موفقیت آمیز
@endsection

@section('content')
<div class="success">
    <p>
        {{ $message }}
    </p>
    <a href="#">
        کانال انجمن علمی مهندسی مکانیک
    </a>
</div>
@endsection