from django import template
register = template.Library()

@register.filter
def compare(i,j):
    return i%j==0