from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def media_filter(value):
    if value:
        return mark_safe(value.url)
    return ""


@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
