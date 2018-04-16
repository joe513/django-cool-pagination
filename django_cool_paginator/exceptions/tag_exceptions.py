"""
These exceptions relate to django-cool-pagination.

"""


class PageNotSpecified(Exception):
    """Raises in case if page wasn't specified at all"""
    pass


class RequestNotExists(Exception):
    """Raises in case if user has forgotten to include request context processor"""
    pass
