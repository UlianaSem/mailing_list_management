from django import template

register = template.Library()


@register.filter()
def cut_string(text, length):
    return text[:length]


@register.filter()
def mediapath(path):
    if path:
        return f'/media/{path}'

    return '/static/img/empty.jpg'
