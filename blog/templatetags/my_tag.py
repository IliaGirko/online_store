from django import template

register = template.Library()


@register.filter
def media_fil(path):
    if path:
        return f"/media/{path}/"
    return "#"
