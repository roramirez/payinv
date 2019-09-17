from core import utils
from django import template


register = template.Library()

# Customs tags and filters


@register.filter
def yes_or_no(value):
    return utils.yes_or_no(value)
