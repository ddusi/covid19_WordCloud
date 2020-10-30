from django import template
register = template.Library()

@register.filter
def slice(List, i):
    return List[i]