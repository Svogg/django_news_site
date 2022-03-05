# from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Caregory
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import Http404


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.all()
#     context = {'news': news,
#                'title': 'Список новостей',
#                }
#     return HttpResponse(render(request, 'news/index.html', context))


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Caregory.objects.get(pk=self.kwargs['category_id'])
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True).select_related('category')
    

# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Caregory.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, template_name='news/category.html', context=context)

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'
    

# def view_news(request, news_id):
#     try:
#         news_item = News.objects.get(pk=news_id)
#     except News.DoesNotExist:
#         raise Http404('No Model matches the given query.')
#     return render(request, 'news/view_news.html', {'news_item': news_item})

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    raise_exception = True

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
