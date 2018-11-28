import codecs,re
import helpers
from defaults import DEFAULT_LANGUAGE, DATA_DIR, LANG_DIR



def save_unique_words(filename,lang=DEFAULT_LANGUAGE):

    # TODO

    existing = []
    unique = []

    with open(DATA_DIR+'/words/eng') as word_file:
        existing = word_file.read().splitlines()



    with codecs.open(filename, encoding='utf-8', errors='ignore') as the_file:
        doc = the_file.read()
        lines = doc.splitlines()
        words = []
        for line in lines:
            words = re.split(r'\W+',line)
            for word in words:
                word = word.strip()
                if word not in existing and word not in unique: unique.append(word)

    with open(DATA_DIR+'/words/'+lang,'a+') as word_file:
        for word in unique: word_file.write(word+'\n')

    return filename


start_time = 
save_unique_words(LANG_DIR+'/eng/txt/pride.txt')