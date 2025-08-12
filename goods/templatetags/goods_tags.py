from django import template
from django.core.paginator import Paginator
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def get_proper_elided_page_range(p, number, on_each_side=1, on_ends=1):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(number=number, on_each_side=on_each_side, on_ends=on_ends)

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

@register.filter()
def is_int(value):
    return isinstance(value, int)