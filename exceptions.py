class Error(Exception):
    # Base class for exception
    # Include as parameter to custom exception class
    pass

class UserNotFound(Error):
    # user == None
    pass

class EmptyBookList(Error):
    # expected paths to books (.txt)
    pass