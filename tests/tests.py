from django.test import SimpleTestCase
from django.http import HttpRequest
from django.template import Template, Context
from django.core.paginator import Paginator

from django_cool_paginator.templatetags import paginator_tags
from django_cool_paginator.exceptions import PageNotSpecified, RequestNotExists

# TODO Optimize Paginator Tag testing


class PaginatorTagTest(SimpleTestCase):

    load = '{% load paginator_tags %}'

    def setUp(self):
        self.paginator = Paginator([str(x) for x in range(30)], 5)
        self.request = HttpRequest()

    def test_ellipsis_or_number(self):
        template_string = Template(self.load + '{% ellipsis_or_number page_obj.paginator page_numb %}')
        page = self.paginator.get_page(4)

        self.request.GET['page'] = 5

        template = template_string.render(Context({'request': self.request, 'page_obj': page, 'page_numb': 5}))
        self.assertEqual(int(template), 5)

        template = template_string.render(Context({'request': self.request, 'page_obj': page, 'page_numb': 8}))
        self.assertEqual(template, '...')

        self.request.GET['page'] = 1

        template = template_string.render(Context({'request': self.request, 'page_obj': page, 'page_numb': 7}))
        self.assertEqual(template, str(None))

    def test_url_replace(self):
        template_string = Template(self.load + "{% url_replace 'page' number %}")

        template = template_string.render(Context({'request': self.request, 'number': 2}))
        self.assertEquals(template, 'page=2')

    def test_size(self):
        template_string = Template(self.load + '{% size size %}')

        template = template_string.render(Context({'size': 'LARGE'}))
        self.assertEqual(template, 'pagination-lg')

        #                               By default
        template = template_string.render(Context())
        self.assertEqual(template, 'pagination-sm')

    def test_previous_name(self):
        template_string = Template(self.load + "{% previous_name name=previous_name %}")

        template = template_string.render(Context({'previous_name': 'Bobby'}))
        self.assertEqual(template, 'Bobby')

        #                               By default
        template = template_string.render(Context())
        self.assertEqual(template, paginator_tags.COOL_PAGINATOR_PREVIOUS_NAME)

    def test_next_name(self):
        template_string = Template(self.load + "{% next_name name=next_name %}")

        template = template_string.render(Context({'next_name': 'Jack'}))
        self.assertEqual(template, 'Jack')

        #                               By default
        template = template_string.render(Context({}))
        self.assertEqual(template, paginator_tags.COOL_PAGINATOR_NEXT_NAME)


class CoolPaginateTest(SimpleTestCase):

    load = '{% load cool_paginate %}'

    def setUp(self):
        self.paginator = Paginator([... for _ in range(5)], 1)
        self.page = self.paginator.get_page(2)
        self.request = HttpRequest()

    def test_page(self):
        template_string = Template(self.load + '{% cool_paginate page=page %}')
        self.assertTrue(template_string.render(Context({'request': self.request, 'page': self.page})))

        #                               Request doesn't exist
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
