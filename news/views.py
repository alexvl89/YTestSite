from django.shortcuts import render
from django.http import HttpResponse

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
        'categories': categories,
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
    categories = Category.objects.all()
    category=Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})