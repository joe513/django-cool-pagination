from django.test import SimpleTestCase
from django.http import HttpRequest
from django.template import Template, Context
from django.core.paginator import Paginator

from django_cool_paginator.templatetags import paginator_tags

# TODO Optimize Paginator Tag testing


class PaginatorTagTest(SimpleTestCase):

    source_template = '{% load paginator_tags %}'

    def setUp(self):
        self.paginator = Paginator([str(x) for x in range(30)], 5)
        self.request = HttpRequest()

    def test_ellipsis_or_number(self):
        template_string = Template(self.source_template + '{% ellipsis_or_number page_obj.paginator page_numb %}')
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
        template_string = Template(self.source_template + "{% url_replace 'page' number %}")

        template = template_string.render(Context({'request': self.request, 'number': 2}))
        self.assertEquals(template, 'page=2')

    def test_size(self):
        template_string = Template(self.source_template + '{% size size %}')

        template = template_string.render(Context({'size': 'LARGE'}))
        self.assertEqual(template, 'pagination-lg')

        #                               By default
        template = template_string.render(Context())
        self.assertEqual(template, 'pagination-sm')

    def test_previous_name(self):
        template_string = Template(self.source_template + "{% previous_name name=previous_name %}")

        template = template_string.render(Context({'previous_name': 'Bobby'}))
        self.assertEqual(template, 'Bobby')

        #                               By default
        template = template_string.render(Context())
        self.assertEqual(template, paginator_tags.COOL_PAGINATOR_PREVIOUS_NAME)

    def test_next_name(self):
        template_string = Template(self.source_template + "{% next_name name=next_name %}")

        template = template_string.render(Context({'next_name': 'Jack'}))
        self.assertEqual(template, 'Jack')

        #                               By default
        template = template_string.render(Context({}))
        self.assertEqual(template, paginator_tags.COOL_PAGINATOR_NEXT_NAME)
