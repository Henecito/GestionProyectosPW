from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Para que aparezca los estados del modelo
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

# Colores para las badges
@register.filter(name='estado_badge')
def estado_badge(estado):
    if not estado:
        return ''
    
    badge_style = f'background-color: {estado.color or "#6c757d"}; color: white; padding: 0.25em 0.5em; border-radius: 0.25rem;'
    return mark_safe(f'<span class="badge" style="{badge_style}">{estado.nombre}</span>')

# Para que el usuario con la actividad asignada pueda editar
@register.filter(name='can_edit_activity')
def can_edit_activity(actividad, user):
    """
    Check if the user can edit the activity
    - Has permission to change activity OR
    - Is the assigned person for the activity
    """
    if not user or not actividad:
        return False
    
    # Check if the user is the assigned person
    if actividad.encargado and actividad.encargado.user == user:
        return True
    
    # Check Django permissions
    return user.has_perm('proyectoApp.change_actividad')