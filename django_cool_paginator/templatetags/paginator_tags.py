"""
Tags for pagination template which is templates directory

These are internal pagination custom tag functions that are needed by paginator template (__paginator.html)
which is in templates directory. User doesn't have to interact with them. They are designed as internal.

Most of them depend on project settings.

Items:
    Vars:
        - COOL_PAGINATOR_NEXT_NAME
        - COOL_PAGINATOR_PREVIOUS_NAME
        - COOL_PAGINATOR_SIZE

    Functions:
        - url_replace(context, field, value)
        - ellipsis_or_number(context, paginator, current_page)
        - size(chosen_size=None)
        - next_name(name=None)
        - previous_name(name=None)

Description:
    Function description:

        url_replace:
            To avoid GET params loosing
        ellipsis_or_number:
            To avoid display a long page table
        size:
            Points to pagination table size.

"""

from django import template
from django.conf import settings


register = template.Library()


#                                                     Pagination settings

COOL_PAGINATOR_NEXT_NAME = getattr(settings, 'COOL_PAGINATOR_NEXT_NAME', 'Next')
COOL_PAGINATOR_PREVIOUS_NAME = getattr(settings, 'COOL_PAGINATOR_PREVIOUS_NAME', 'Previous')
COOL_PAGINATOR_SIZE = getattr(settings, 'COOL_PAGINATOR_SIZE', None)

#                                                           Tags...


# next_name tag
next_name = register.simple_tag(name='next_name', func=lambda name=None: name or COOL_PAGINATOR_NEXT_NAME)

# previous_name tag
previous_name = register.simple_tag(name='previous_name', func=lambda name=None: name or COOL_PAGINATOR_PREVIOUS_NAME)


@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    """
    To avoid GET params losing

    :param context: context_obj
    :param field: str
    :param value: str
    :return: dict-like object
    """

    query_string = context['request'].GET.copy()
    query_string[field] = value

    return query_string.urlencode()


# TODO Make this function maximum customizable
@register.simple_tag(takes_context=True)
def ellipsis_or_number(context, paginator, current_page):
    """
    To avoid display a long pagination bar

    :param context: template context
    :param paginator: paginator_obj
    :param current_page: int
    :return: str or None
    """

    # Checks is it first page
    chosen_page = int(context['request'].GET['page']) if 'page' in context['request'].GET else 1

    if current_page in (chosen_page + 1, chosen_page + 2, chosen_page - 1, chosen_page - 2,
                        paginator.num_pages, paginator.num_pages - 1, 1, 2, chosen_page):
        return current_page

    if current_page in (chosen_page + 3, chosen_page - 3):
        return '...'


@register.simple_tag
def size(chosen_size=None):
    """
    Points to pagination bar size.

    :param chosen_size: int
    :return: str
    """

    return {
        'LARGE': 'pagination-lg',
        'SMALL': 'pagination-sm',
    }.get(chosen_size or COOL_PAGINATOR_SIZE, '')
