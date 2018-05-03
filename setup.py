import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-cool-pagination',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Simple pagination app that saves your time.',
    long_description_content_type='text/markdown',
    long_description=README,
    url='https://github.com/joe513/django-cool-pagination',
    author='Jabrail Lezgintsev',
    author_email='lezgintsev13@yandex.ru',
    keywords='python3 django pagination bootstrap4',
    project_urls={
        'Source': 'https://github.com/joe513/django-cool-pagination'
    },
    python_requires='>=3',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
