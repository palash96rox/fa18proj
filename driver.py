import os
import datetime
import builder
import helpers
import pprint

LIB_DIR = os.path.join(os.getcwd(),'lib')

def build():
    invalids = dict()

    # Get book library
    library = dict()
    for dir in os.listdir(os.path.join(LIB_DIR,'lang')):
        library[dir] = []
        with open(os.path.join(LIB_DIR,'lang/'+dir+'/invalid.txt')) as invalid_chars:
            invalids[dir] = invalid_chars.read().splitlines()
        for files in os.listdir(os.path.join(LIB_DIR,'lang/'+dir+'/txt')):
            if files.endswith('txt'):
                path = os.path.join(LIB_DIR,'lang/'+dir+'/txt/'+files)
                library[dir].append(path)

    # Get user library
    users = dict()
    for dir in os.listdir(os.path.join(LIB_DIR,'users')):
        users[dir] = []
        with open(os.path.join(LIB_DIR,'users/'+dir+'/invalid.txt')) as invalid_chars:
            invalids[dir] = invalid_chars.read().splitlines()
        for files in os.listdir(os.path.join(LIB_DIR,'users/'+dir+'/txt')):
            if files.endswith('txt'):
                path = os.path.join(LIB_DIR,'users/'+dir+'/txt/'+files)
                users[dir].append(path)

    # Get illegal characters
    illegal_chars = []
    for typ in invalids.keys():
        illegal_chars = helpers.merge_lists([invalids[typ],illegal_chars])

    # Build tries
    books_data = builder.trie_builder(library,illegal_chars)
    users_data = builder.trie_builder(users,illegal_chars)

    # Update files at 0420hrs
    if str(datetime.datetime.now().time())[:5] == '04:20':
        builder.update_files(books_data)
        builder.update_files(users_data)

    return books_data,users_data

books,users = build()
