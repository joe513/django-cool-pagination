#!/usr/bin/env python

import os
import sys

import django

from django.conf import settings
from django.test.utils import get_runner


def run_tests():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    run_tests()
