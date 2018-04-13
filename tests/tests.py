from django.test import SimpleTestCase
from django.http import HttpRequest
from django.template import Template, Context
from django.core.paginator import Paginator

from django_cool_paginator.templatetags import paginator_tags

# TODO Optimize Paginator Tag testing


class PaginatorTagTest(SimpleTestCase):

    Template = Template("{% load paginator_tags %} {% ellipsis_or_number page_obj.paginator current_page %}")

    def setUp(self):
        paginator = Paginator([str(x) for x in range(30)], 5)
        page = paginator.get_page(3)
        template = self.Template.render(Context({'request': HttpRequest(), 'page_obj': page, 'current_page': 4}))

    def test_size(self):
        self.assertEqual(paginator_tags.size(), 'pagination-lg')

    def test_next_name(self):
        self.assertEqual(paginator_tags.next_name(), 'Next')

    def test_previous_name(self):
        self.assertEqual(paginator_tags.previous_name(), 'Previous')

    def test_ellipsis_or_number(self):
        ...
