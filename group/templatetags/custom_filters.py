from django import template

from utils.custom_functions import plural_records

register = template.Library()


@register.filter(name='plural_records')
def plural_records(num: str):
    return plural_records(num)
