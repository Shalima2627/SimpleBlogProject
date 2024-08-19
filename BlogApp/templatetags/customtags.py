from django import template
from ..models import Category
from django.template.defaultfilters import stringfilter
import markdown as md

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])
