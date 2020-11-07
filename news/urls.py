#Маршрутизация на http://127.0.0.1/news/
from django.urls import path
# from django.contrib import admin
#импортируем из views.py написанные функции
from .views import *


# admin.news.site_header  = 'Coffeehouse admin'


#указывает маршрут на функцию index, test
urlpatterns=[
    path('',index),
    # <int:category_id>/ - адрес категории при переходе открывается функция get_category
    path('category/<int:category_id>/',get_category),
    #path('test/',test),

]

# url(r'^admin/', admin.site.urls),