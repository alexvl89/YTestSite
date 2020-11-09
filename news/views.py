from django.http import request
from django.shortcuts import render
from django.http import HttpResponse

# модуль для ошибки 404
from django.shortcuts import get_object_or_404

from .models import News, Category

# Create your views here.
#request - разные данные 
def index(request):
    news=News.objects.order_by('-created_at')
    #res='<h1>Список новостей</h1>\n'
    categories = Category.objects.all()
    #доб данных для отправки в шаблон
    context={
        'news':news,
        'title': 'Список новостей',
        # закомменирован т.к. добавлено в _sidebar.html импортирование тега
        # 'categories': categories,
    }
    return render(request,'news/index.html',context)

    #return render(request,'news/index.html',{'news':news,'title':'Список новостей'})

    #for item in news:
    #    res+=f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
    #return HttpResponse(res)


#def test(request):
#    return HttpResponse('<h1>Тестовая страница</h1>')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

# def my_view(request):
    # obj = get_object_or_404(MyModel, pk=1)