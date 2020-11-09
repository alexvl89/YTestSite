from django.db import models

# подключение модуля для построение ссылок
from django.urls import reverse

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
    title = models.CharField(max_length=150, verbose_name='Наименование')
    #blank=true не обязателен к заполнению
    content = models.TextField(blank=True, verbose_name='Контент')
    #дата создание новости меняться не будет auto_now_add=True
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') 
    #дата создание/изменение новости меняться будет auto_now=True
    update_at=models.DateTimeField(auto_now=True, verbose_name='Обновлено') 
    #сохранение файла картинки (путь папки по структуре даты)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    #одобрено к публикации
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    #поле первичного ключа для таблицу Category. on_delete=models.PROTECT - защита от удаляния
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')


    def my_fun(self):
        return 'Hello from model'

    
    def __str__(self):
        return self.title

    # стандарное название метода для опеределения в python
    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})
    

    class Meta:
        #Наименование модели в единственном числе
        verbose_name='Новость'
        verbose_name_plural='Новости'
        #сортировка данных в админке
        ordering=['-created_at']


class Category(models.Model):
    #атрибут db_index=True индексирует поле
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    #стандарное представление чтобы показывало в значение
    def __str__(self):
        return self.title

    # стандарное название метода для опеределения в python
    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})
    


    class Meta:
        #Наименование модели в единственном числе
        verbose_name='Категория'
        #Наименование модели во множественном числе
        verbose_name_plural='Категории'
        #сортировка данных в админке
        ordering=['title']


