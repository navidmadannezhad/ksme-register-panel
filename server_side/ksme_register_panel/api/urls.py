from collections import UserList
from django.contrib import admin
from django.urls import path, include
from .views.levelViews import UsersList, Level1, Level2, Level3, Activate

urlpatterns = [
    path('level1/', Level1.as_view()),
    path('level2/', Level2.as_view()),
    path('level3/', Level3.as_view()),
    path('activate/<uidb64>/<token>/', Activate.as_view(), name='activate'),
]
