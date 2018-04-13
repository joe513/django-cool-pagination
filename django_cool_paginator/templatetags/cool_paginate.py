from django import template

from django_cool_paginator.exceptions import PaginatorNotSpecified
# TODO To discuss which name is better for the module: cool_paginate or cool_pagination

register = template.Library()


@register.inclusion_tag('__paginators/paginator.html', takes_context=True)
def cool_paginate(context, page_obj=None, size=None, next_name=None, previous_name=None):
    return_dict = {
        'request': context['request'],
        'size': size,
        'next_name': next_name,
        'previous_name': previous_name,
    }

    if page_obj is not None:
        return_dict['page_obj'] = page_obj
    else:
        try:
            return_dict['page_obj'] = context['page_obj']
        except KeyError:
            raise PaginatorNotSpecified("You customized paginator standard name, "
                                        "but haven't specified it in {% cool_paginate %} tag.")

    return return_dict
