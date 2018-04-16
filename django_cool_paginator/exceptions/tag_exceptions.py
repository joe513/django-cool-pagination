"""
These exceptions relate to django-cool-pagination.

Items:
    Exceptions:
        - PageNotSpecified(*args, **kwargs)
        - RequestNotExists(*args, **kwargs)

Description:
    Exception Description:

        PageNotSpecified:
            Raises in case if page wasn't specified at all

        RequestNotExists:
            Raises in case if user has forgotten to include request context processor

"""


class PageNotSpecified(Exception):
    """Raises in case if page wasn't specified at all"""
    pass


class RequestNotExists(Exception):
    """Raises in case if user has forgotten to include request context processor"""
    pass
