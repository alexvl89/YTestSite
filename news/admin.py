from django.contrib import admin

# Register your models here.

from .models import News, Category

#класс для добавления в админ панели столбцов таблицы.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'created_at','update_at','is_published')
    #ссылки на изменение новости при нажатии на id или названию новости
    list_display_links = ('id', 'title')
    #поиск по полям
    search_fields = ('title', 'content')
    #редактируемые поля (чтобы редактировать в списке)
    list_editable = ('is_published',)
    #для фильтрования
    list_filter = ('is_published','category')

#admin.site.register(News)


#класс для добавления в админ панели столбцов таблицы Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    #ссылки на изменение новости при нажатии на
    list_display_links = ('id', 'title')
    #поиск по полям
    search_fields = ('title',)



#Регистрируем поля в таблице
admin.site.register(News, NewsAdmin)
admin.site.register(Category,CategoryAdmin)



