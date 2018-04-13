"""
Tags for pagination template which is in templates/__paginators

Based on project settings.
"""

from django import template
from django.conf import settings


# TODO IMPROVE ALL THE DOCSTRINGS!

register = template.Library()


# PAGINATION_SETTINGS

COOL_PAGINATOR_NEXT_NAME = getattr(settings, 'COOL_PAGINATOR_NEXT_NAME', 'Next')
COOL_PAGINATOR_PREVIOUS_NAME = getattr(settings, 'COOL_PAGINATOR_PREVIOUS_NAME', 'Previous')
COOL_PAGINATOR_SIZE = getattr(settings, 'COOL_PAGINATOR_SIZE', None)


# Tags...


# next_name tag
next_name = register.simple_tag(name='next_name', func=lambda name=None: COOL_PAGINATOR_NEXT_NAME
                                if name is None else name)

# previous_name tag
previous_name = register.simple_tag(name='previous_name', func=lambda name=None: COOL_PAGINATOR_PREVIOUS_NAME
                                    if name is None else name)


@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    """
    To avoid GET params loosing

    :param context:
    :param field:
    :param value:
    :return: dict-like object
    """

    query_string = context['request'].GET.copy()
    query_string[field] = value

    return query_string.urlencode()


@register.simple_tag(takes_context=True)
def ellipsis_or_number(context, paginator, current_page):

    """
    To avoid display a long page table

    :param context: template context
    :param paginator: Paginator obj
    :param current_page: int
    :return: str or None

    """

    # Checks is it first page
    chosen_page = int(context['request'].GET['page']) if 'page' in context['request'].GET else 1

    if current_page == chosen_page:
        return chosen_page

    if current_page in (chosen_page + 3, chosen_page - 3):
        return '...'

    if current_page in (chosen_page + 1, chosen_page + 2, chosen_page - 1,
                        chosen_page - 2, paginator.num_pages, paginator.num_pages - 1, 1, 2):
        return current_page


@register.simple_tag
def size(chosen_size=None):
    """
    Points to pagination table size.

    :return: str or None
    """

    if chosen_size == 'LARGE':
        return 'pagination-lg'
    if chosen_size == 'SMALL':
        return 'pagination-sm'
    if COOL_PAGINATOR_SIZE == 'LARGE':
        return 'pagination-lg'
    if COOL_PAGINATOR_SIZE == 'SMALL':
        return 'pagination-sm'
    return ''
