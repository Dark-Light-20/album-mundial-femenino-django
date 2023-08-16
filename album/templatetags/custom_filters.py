from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='replace_comma')
@stringfilter
def replace_comma(value):
    return value.replace(',', '.')
