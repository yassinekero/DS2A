from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]

@register.filter
def increment(indexable, num):
    inc = indexable + num
    return inc



@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)


@register.filter
def hash(h, key):
    return h[key]

@register.filter
def get_value_from_dict(dictionary, key):
    return dictionary.get(key)