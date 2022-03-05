from django import template
from news.models import Caregory
from django.db.models import *
register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Caregory.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Caregory.objects.all()
    categories = Caregory.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories': categories}
