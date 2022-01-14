from django import template
from news.models import Caregory

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Caregory.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='World'):
    categories = Caregory.objects.all()
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}
