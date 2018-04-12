from django.test import SimpleTestCase
from django.http import HttpRequest

from django_cool_paginator.templatetags import paginator_tags


class PaginatorTagTest(SimpleTestCase):

    def test_size(self):
        self.assertEqual(paginator_tags.size(), 'pagination-lg')

    def test_next_name(self):
        self.assertEqual(paginator_tags.next_name(), 'Next')

    def test_previous_name(self):
        self.assertEqual(paginator_tags.previous_name(), '&laquo;')

    # def test_