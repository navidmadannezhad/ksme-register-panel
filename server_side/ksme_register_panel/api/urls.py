from collections import UserList
from django.contrib import admin
from django.urls import path, include
from .views import UsersList, Level1

urlpatterns = [
    path('', Level1.as_view())
]

# داری ویژگی های یوزر ها رو وارد دیتابیس میکنی که بعد سریالایزر ها رو بسازی.
