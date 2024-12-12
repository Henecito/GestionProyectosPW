from django import template
from django.utils.safestring import mark_safe

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

@register.filter(name='estado_badge')
def estado_badge(estado):
    """
    Renders a badge with the estado's name and color
    """
    if not estado:
        return ''
    
    # Use inline styles to apply the estado's color
    badge_style = f'background-color: {estado.color or "#6c757d"}; color: white; padding: 0.25em 0.5em; border-radius: 0.25rem;'
    return mark_safe(f'<span class="badge" style="{badge_style}">{estado.nombre}</span>')