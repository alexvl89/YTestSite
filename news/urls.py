#Маршрутизация на http://127.0.0.1/news/
from django.urls import path

#импортируем из views.py написанные функции
from .views import *

#указывает маршрут на функцию index, test
urlpatterns=[
    path('',index),
    #path('test/',test),

]