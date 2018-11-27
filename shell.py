import os, cmd, sys
from app import App
from consts import DEFAULT_LIBRARY

class AutocompleteShell(cmd.Cmd):
    intro = 'Welcome to the autocomplete shell. Type ? for help!'
    prompt = '(autocomplete) '
    file = None
    data = None

    def __init__(self, file=None, data=dict()):
        self.data = data
        self.file = file

    # Basic commands
    def do_exit(self, arg):
        'Exit the program'
        print('Bye')
        return True # TODO

    def do_complete(self, arg):
        pass

    def do_build(self, arg=DEFAULT_LIBRARY):
        

    # Utility
    def preloop(self):
        super(AutocompleteShell,self).preloop()

    def postloop(self):
        # TODO save to file and call the 
        super(AutocompleteShell,self).postloop()

def trial():
    shell = AutocompleteShell()
    shell.cmdloop()


if __name__ == '__main__':
    trial()