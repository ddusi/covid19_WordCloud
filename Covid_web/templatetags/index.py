from django import template
register = template.Library()

@register.filter
def index(List):
    return range(len(List))