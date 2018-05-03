"""
Main module for pagination purpose

This module is designed as main. To load it to your template just write:

                        {% load cool_paginate %}

Items:
    Functions:

        - cool_paginate(context, **kwargs)

Description:
    Function description:

        cool_paginate:
            Main function for pagination process.

"""

from django import template

from django_cool_paginator.exceptions import PageNotSpecified, RequestNotExists
from django.conf import settings

# TODO Discuss which name is better for the module cool_paginate or cool_pagination

register = template.Library()


@register.inclusion_tag('__paginator.html', takes_context=True)
def cool_paginate(context, **kwargs):
    """Main function for pagination process."""

    names = (
        'size',
        'next_name',
        'previous_name',
        'elastic',
        'page_obj',
    )

    return_dict = {name: value for name, value in zip(names, map(kwargs.get, names))}

    if context.get('request'):
        return_dict['request'] = context['request']
    else:
        raise RequestNotExists(
            'Unable to find request in your template context,'
            'please make sure that you have the request context processor enabled'
        )

    if not return_dict.get('page_obj'):
        if context.get('page_obj'):
            return_dict['page_obj'] = context['page_obj']
        else:
            raise PageNotSpecified(
                'You customized paginator standard name, '
                "but haven't specified it in {% cool_paginate %} tag."
            )

    if not return_dict.get('elastic'):
        return_dict['elastic'] = getattr(settings, 'COOL_PAGINATOR_ELASTIC', 10)

    return return_dict
