from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Caregory
from .forms import NewsForm
from django.http import Http404


def index(request):
    news = News.objects.all()
    context = {'news': news,
               'title': 'Список новостей',
    }
    return HttpResponse(render(request, 'news/index.html', context))


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Caregory.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    try:
        news_item = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404('No Model matches the given query.')
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})