from django.urls import path, include
from .views import HomePage, programm

app_name = 'page'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('result/', programm, name='result'),
]
