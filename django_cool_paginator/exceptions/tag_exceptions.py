class PaginatorNotPointed(Exception):

    def __init__(self, text):
        super(PaginatorNotPointed, self).__init__(text)
