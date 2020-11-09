from django import template

from news.models import Category


register = template.Library()

# функция получения всех категорий
@register.simple_tag(name='get_list_categories') #декаратор для изменения названия нашего тега
def get_categories():
    return Category.objects.all()



@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
    # return {"categories": categories, "arg1": arg1, "arg2": arg2}
