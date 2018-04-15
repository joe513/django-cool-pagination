"""
These exceptions relate to django-cool-pagination.

"""


class PaginatorNotSpecified(Exception):
    """Raised in case if Paginator wasn't specified at all"""
    pass


class RequestNotExists(Exception):
    """Raised in case if user has forgotten to include request context processor"""
    pass
