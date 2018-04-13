from django import template

from django_cool_paginator.exceptions import PaginatorNotSpecified, RequestNotExists
# TODO To discuss which name is better for the module cool_paginate or cool_pagination

register = template.Library()


@register.inclusion_tag('__paginators/paginator.html', takes_context=True)
def cool_paginate(context, page=None, size=None, next_name=None, previous_name=None):
    return_dict = {
        'size': size,
        'next_name': next_name,
        'previous_name': previous_name,
    }
    try:
        return_dict['request'] = context['request']
    except KeyError:
        raise RequestNotExists(
            'Unable to find request in your template context,'
            'please make sure that you have the request context processor enabled'
        )

    if page is not None:
        return_dict['page_obj'] = page
    else:
        try:
            return_dict['page_obj'] = context['page_obj']
        except KeyError:
            raise PaginatorNotSpecified(
                'You customized paginator standard name, '
                "but haven't specified it in {% cool_paginate %} tag."
            )

    return return_dict
