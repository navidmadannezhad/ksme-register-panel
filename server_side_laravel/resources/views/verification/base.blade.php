<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title')</title>
    <style>
        div.verification-message{
            width: 100%;
            direction: rtl;
            background-color: #1b1b1b;
            font-size: 1.5rem;
            padding: 50px 0px;
        }
        div.verification-message p{
            text-align: center;
            color: white;
            font-size: 1.3rem;
        }
        div.verification-message form{
            width: 100%;
            text-align: center;
        }
        div.verification-message form input{
            padding: 10px 20px;
            background-color: #fff85c;
            border: none;
            border-radius: 5px;
            color: black;
            font-size: 1.5rem;
        }
    </style>
</head>
<body>
    @yield('content')
</body>
</html>