from django import template
import string

register = template.Library()

@register.filter(name='splitlines')
def splitlines(value):
    """Split text into lines"""
    if value:
        return value.split('\n')
    return []

@register.filter(name='split')
def split(value, arg):
    """Split a string by delimiter"""
    return value.split(arg)

@register.filter(name='trim')
def trim(value):
    """Remove leading and trailing whitespace"""
    if value:
        return value.strip()
    return ''