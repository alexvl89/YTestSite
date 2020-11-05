from django.shortcuts import render
from django.http import HttpResponse

from .models import News

# Create your views here.
#request - разные данные 
def index(request):
    news=News.objects.order_by('-created_at')
    #res='<h1>Список новостей</h1>\n'
    context={
        'news':news,
        'title': 'Список новостей',
    }
    return render(request,'news/index.html',context)

    #return render(request,'news/index.html',{'news':news,'title':'Список новостей'})

    #for item in news:
    #    res+=f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
    #return HttpResponse(res)


#def test(request):
#    return HttpResponse('<h1>Тестовая страница</h1>')


