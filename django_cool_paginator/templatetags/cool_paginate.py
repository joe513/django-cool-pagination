from django import template

from django_cool_paginator.exceptions import PaginatorNotPointed

register = template.Library()


@register.inclusion_tag('__paginators/paginator.html', takes_context=True)
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
