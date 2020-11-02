from django.db import models

# Create your models here.
#Описание атрибутов - полей таблицы для новостей

#id - INT
#title - Varchar
#content - Text
#created_at - DataTime
#update_at - DataTime
#photo - Image
#is_published - Boolean

#Создаем класс новостей
class News(models.Model):
    #Создаем атрибуты выше
    title = models.CharField(max_length=150)
    #blank=true не обязателен к заполнению
    content = models.TextField(blank=True)
    #дата создание новости меняться не будет auto_now_add=True
    created_at=models.DateTimeField(auto_now_add=True) 
    #дата создание/изменение новости меняться будет auto_now=True
    update_at=models.DateTimeField(auto_now=True) 
    #сохранение файла картинки (путь папки по структуре даты)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    #одобрено к публикации
    is_published = models.BooleanField(default=True)