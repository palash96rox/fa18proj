from constanrs import USERS_DIR

class User():
    def __init__(self, ID='', pref=dict(), library=dict(), scripts=USERS_DIR):
        self.ID = ID
        self.pref = pref
        self.library = library
        self.scripts = scripts
