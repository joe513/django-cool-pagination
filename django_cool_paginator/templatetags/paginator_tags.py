from django import template
from django.conf import settings

from django_cool_paginator.exceptions import PaginatorNotPointed

register = template.Library()


# TODO IMPROVE ALL THE DOCSTRINGS!


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
def size():
    """
    Points to pagination table size.

    :return: str or None
    """

    if hasattr(settings, 'COOL_PAGINATOR_SIZE'):
        if settings.COOL_PAGINATOR_SIZE == 'LARGE':
            return 'pagination-lg'
        if settings.COOL_PAGINATOR_SIZE == 'SMALL':
            return 'pagination-sm'


@register.inclusion_tag('paginators/paginator.html', takes_context=True)
def cool_paginate(context, page_obj=None):
    return_dict = {
        'request': context['request'],
    }

    if page_obj is not None:
        return_dict['page_obj'] = page_obj
    else:
        try:
            return_dict['page_obj'] = context['page_obj']
        except KeyError:
            raise PaginatorNotPointed("You customized standard paginator name, "
                                      "but didn't point it in {% cool_paginate %} tag.")

    return return_dict
