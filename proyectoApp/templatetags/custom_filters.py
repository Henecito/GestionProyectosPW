from django import template

register = template.Library()

@register.filter
def lookup(obj, attr):
    try:
        value = getattr(obj, attr)
        return value if value is not None else ''
    except AttributeError:
        return ''
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')
