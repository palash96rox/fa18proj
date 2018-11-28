from consts import USERS_DIR
from app import Session

class User():
    def __init__(self, ID='', pref=dict(), library=dict(), scripts=USERS_DIR):
        self.ID = ID
        self.pref = pref
        self.library = library
        self.scripts = scripts
        self.sessions = []
        self.current_session = Session()

    def make_library(self):
        pass
