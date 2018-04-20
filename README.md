# django-cool-pagination

[![Build Status](https://travis-ci.org/joe513/django-cool-pagination.svg?branch=master)](https://travis-ci.org/joe513/django-cool-pagination)
[![Coverage Status](https://coveralls.io/repos/github/joe513/django-cool-pagination/badge.svg?branch=master)](https://coveralls.io/github/joe513/django-cool-pagination?branch=master)
[![PyPI version](https://badge.fury.io/py/django-cool-pagination.svg)](https://badge.fury.io/py/django-cool-pagination)

*django-cool-pagination* is simple pagination app that saves your time.

## WARNING:
 **The project is on development stage, some things may not work properly.**
## Prerequisites
Currently it supports Bootstrap 4.x only. So that you have to add [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/download) to your project.

## Installing:
### PIP

    pip install django-cool-pagination

## Using

### View
#### FBV (Function based view)

    def listing(request):
        contact_list = Contacts.objects.all()
        paginator = Paginator(contact_list, 25)

        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        return render(request, 'list.html', {'page_obj': page_obj})

#### CBV (Class based view)

    class Listing(ListView):
        model = Item
        paginate_by = 5

### Template
    {% load cool_paginate %}
    
    {% for contact in page_obj %}
        ...
    {% endfor %}
    
    {% cool_paginate %}



## License
This project is licensed under the MIT License - see the LICENSE file for details
