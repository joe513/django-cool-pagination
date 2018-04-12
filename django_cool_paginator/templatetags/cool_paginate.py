from django import template

from django_cool_paginator.exceptions import PaginatorNotSpecified

register = template.Library()


@register.inclusion_tag('__paginators/paginator.html', takes_context=True)
def cool_paginate(context, page_obj=None, size=None):
    return_dict = {
        'request': context['request'],
        'size': size
    }

    if page_obj is not None:
        return_dict['page_obj'] = page_obj
    else:
        try:
            return_dict['page_obj'] = context['page_obj']
        except KeyError:
            raise PaginatorNotSpecified("You customized standard paginator name, "
                                        "but haven't specified it in {% cool_paginate %} tag.")

    return return_dict
