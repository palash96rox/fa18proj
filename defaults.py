import os

SRC = os.getcwd()
LIB_DIR = os.path.join(SRC,'lib')
USERS_DIR = os.path.join(LIB_DIR,'users')
LANG_DIR = os.path.join(LIB_DIR,'lang')
DATA_DIR = os.path.join(LIB_DIR,'data')
DEFAULT_LANGUAGE = 'eng'
WORD_ENDERS = (' ','.','!','?',';','\'','\"',':','-') # TODO Change to unicode