#Маршрутизация на http://127.0.0.1/news/
from django.urls import path
# from django.contrib import admin
#импортируем из views.py написанные функции
from .views import *


# admin.news.site_header  = 'Coffeehouse admin'


#указывает маршрут на функцию index, test
# первый аргумент в path - это путь приложения
# name - имя маршрута, чтобы ссылаться с html страниц
# второй аргумент index и get_category - функции в файле views.py
urlpatterns=[
    
    # path('',index),
    # <int:category_id>/ - адрес категории при переходе открывается функция get_category
    
    #path('test/',test),
    
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),

]

# url(r'^admin/', admin.site.urls),






