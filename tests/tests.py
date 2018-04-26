from django.test import SimpleTestCase
from django.http import HttpRequest
from django.template import Template, Context
from django.core.paginator import Paginator

from django_cool_paginator.templatetags import paginator_tags
from django_cool_paginator.exceptions import PageNotSpecified, RequestNotExists


class BaseTest(SimpleTestCase):

    def setUp(self):
        paginator = Paginator([... for _ in range(30)], 5)
        self.page = paginator.page(4)
        self.request = HttpRequest()

        self.base_context = {
            'request': self.request,
            'page_obj': paginator.page(4),
        }

        self.size_conf = {
            'LARGE': 'pagination-lg',
            'SMALL': 'pagination-sm'
        }


class PaginatorTagTest(BaseTest):
    """These tests are designed for paginator_tags.py internal module which is in templatetags"""

    load = '{% load paginator_tags %}'

    def test_ellipsis_or_number(self):
        template_string = Template(self.load + '{% ellipsis_or_number page_obj.paginator page_numb %}')

        self.request.GET['page'] = 5

        context = self.base_context.copy()
        context['page_numb'] = 5

        template = template_string.render(Context(context))
        self.assertEqual(int(template), 5)

        context['page_numb'] = 8

        template = template_string.render(Context(context))
        self.assertEqual(template, '...')

        self.request.GET['page'] = 1
        context['page_numb'] = 7

        template = template_string.render(Context(context))
        self.assertEqual(template, str(None))

    def test_url_replace(self):
        template_string = Template(self.load + "{% url_replace 'page' number %}")

        context = self.base_context.copy()
        context['number'] = 2

        template = template_string.render(Context(context))
        self.assertEquals(template, 'page=2')

    def test_size(self):
        template_string = Template(self.load + '{% size size %}')

        context = {'size': 'LARGE'}

        template = template_string.render(Context(context))
        self.assertEqual(template, self.size_conf[context['size']])

        #                               By default
        template = template_string.render(Context())
        self.assertEqual(template, self.size_conf[paginator_tags.COOL_PAGINATOR_SIZE])

    def test_previous_name(self):
        template_string = Template(self.load + "{% previous_name name=previous_name %}")

        previous_name = 'Bobby'

        template = template_string.render(Context({'previous_name': previous_name}))
        self.assertEqual(template, previous_name)

        #                               By default
        template = template_string.render(Context())
        self.assertEqual(template, paginator_tags.COOL_PAGINATOR_PREVIOUS_NAME)

    def test_next_name(self):
        template_string = Template(self.load + "{% next_name name=next_name %}")

        next_name = 'Jack'

        template = template_string.render(Context({'next_name': next_name}))
        self.assertEqual(template, next_name)

        #                               By default
        template = template_string.render(Context({}))
        self.assertEqual(template, paginator_tags.COOL_PAGINATOR_NEXT_NAME)


class CoolPaginateTest(BaseTest):
    """These tests are designed for cool_paginate function which is in cool_paginate.py module"""

    load = '{% load cool_paginate %}'

    def test_page(self):
        template_string = Template(self.load + '{% cool_paginate %}')
        self.assertTrue(template_string.render(Context(self.base_context.copy())))

    def test_exception(self):
        template_string = Template(self.load + '{% cool_paginate %}')

        with self.assertRaisesMessage(RequestNotExists,
                                      'Unable to find request in your template context,'
                                      'please make sure that you have the request context processor enabled'
                                      ):
            template_string.render(Context())

        with self.assertRaisesMessage(PageNotSpecified,
                                      'You customized paginator standard name, '
                                      "but haven't specified it in {% cool_paginate %} tag."
                                      ):
            template_string.render(Context({'request': self.request}))

    def test_size(self):

        context = self.base_context.copy()
        context['size'] = 'LARGE'

        template_string = Template(self.load + '{% cool_paginate size=size %}')
        template = template_string.render(Context(context))

        self.assertIn(self.size_conf[context['size']], template)

        #                               By default
        context.pop('size')
        template = template_string.render(Context(context))

        self.assertIn(self.size_conf[paginator_tags.COOL_PAGINATOR_SIZE], template)

    def test_next_name(self):

        context = self.base_context.copy()
        context['next_name'] = 'Go to'

        template_string = Template(self.load + '{% cool_paginate next_name=next_name %}')
        template = template_string.render(Context(context))

        self.assertIn(context['next_name'], template)

        #                               By default
        context.pop('next_name')
        template = template_string.render(Context(context))
        self.assertIn(paginator_tags.COOL_PAGINATOR_NEXT_NAME, template)

    def test_previous_name(self):

        context = self.base_context.copy()
        context['previous_name'] = 'Back to'

        template_string = Template(self.load + '{% cool_paginate previous_name=previous_name %}')
        template = template_string.render(Context(context))

        self.assertIn(context['previous_name'], template)

        #                               By default
        context.pop('previous_name')
        template = template_string.render(Context(context))
        self.assertIn(paginator_tags.COOL_PAGINATOR_PREVIOUS_NAME, template)

    def test_elastic(self):

        context = self.base_context.copy()
        context['elastic'] = 5

        standard_template = Template(self.load + '{% cool_paginate elastic=elastic%}').render(Context(context)).strip()

        context['elastic'] = 10
        template = Template(self.load + '{% cool_paginate elastic=elastic%}').render(Context(context)).strip()

        self.assertHTMLNotEqual(template, standard_template)
