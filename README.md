# django-cool-pagination

[![Build Status](https://travis-ci.org/joe513/django-cool-pagination.svg?branch=master)](https://travis-ci.org/joe513/django-cool-pagination)
[![Coverage Status](https://coveralls.io/repos/github/joe513/django-cool-pagination/badge.svg?branch=master)](https://coveralls.io/github/joe513/django-cool-pagination?branch=master)
[![PyPI version](https://badge.fury.io/py/django-cool-pagination.svg)](https://badge.fury.io/py/django-cool-pagination)

*django-cool-pagination* is simple pagination app that saves your time.

## WARNING:
 **The project is still on development stage, some things may not work properly.**
 
 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Old_book_bindings.jpg/1280px-Old_book_bindings.jpg" />

## Prerequisites
Currently it supports Bootstrap 4.x only. So that you have to add [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/download) to your project. <br/>
<img class="center" src="https://i.imgur.com/5FK3tt6.png" />

## Features 
<img class="center" alt="paris" src="https://i.imgur.com/uMNye7P.png" />

   - _Dynamic query string creation_
   - _Length auto control_
   - _Fully customizable_ (aspiring)

## Installation
### Installing
#### pip
    pip install django-cool-pagination
#### setup.py
    git clone https://github.com/joe513/django-cool-pagination.git
    cd django-cool-pagination
    python setup.py install
### Setting up
#### Add to `INSTALLED_APPS`
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        
        'django_cool_paginator'
#### Make sure `request` is in `context_processors`
        'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',

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
    
    {% cool_paginate page_obj=ENTER HERE YOUR PAGE OBJECT! %}

> **Note:**
You don't have to specify `page` if its name is `page_obj` as default.

## Customization
You can customize it so that it works as you want. Customize it by defining settings either in setting.py or 
inside of `{% cool_paginate %} `

#### setting.py

`COOL_PAGINATOR_NEXT_NAME` - Name for "next" button in pagination bar. <br/>
`COOL_PAGINATOR_PREVIOUS_NAME` - Name for "previous" button in pagination bar <br/>
`COOL_PAGINATOR_SIZE` - Size of pagination bar (choose: "LARGE" or "SMALL") <br/>
`COOL_PAGINATOR_ELASTIC` - What page width is elastic mode enabled from?

#### {% cool_paginate page_obj next_name previous_name size elastic %}
`page_obj` - Type here your page object. <br/>
`next_name` - Name for "next" button in pagination bar. <br/>
`previous_name` - Name for "previous" button in pagination bar <br/>
`size` - Size of pagination bar (choose: "LARGE" or "SMALL") <br/>
`elastic` - What page width is elastic mode enabled from?

> **Note:**
> `{% cool_paginate %}` has a priority, _django-cool-pagination_ will firstly look at this, after at setting.py

## License
This project is licensed under the MIT License - see the LICENSE file for details
<hr/>


_inspired by [inoks/m3u8](https://github.com/inoks/m3u8)_
 
