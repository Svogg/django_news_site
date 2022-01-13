from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Caregory


def index(request):
    news = News.objects.all()
    categories = Caregory.objects.all()
    context = {'news': news,
               'title': 'Список новостей',
               'categories': categories
    }
    return HttpResponse(render(request, 'news/index.html', context))


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Caregory.objects.all()
    category = Caregory.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)
