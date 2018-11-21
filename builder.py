# coding=utf-8
# TODO move all to a class and access via object

import codecs
import pprint
from trie import Trie

data = dict()

# Word cleaner
def justWord(word) :
    # print('received--',word)
    invalid = ('.','!','(',')','[',']','{','}','|',',','-','।','\'','_',';',':','\"','”','“')
    if word.endswith(invalid):
        return justWord(word[:len(word)-1])
    if word.startswith(invalid):
        return justWord(word[1:])
    return word


def build(file, lang = 'def') :
    root = Trie()
    freq = dict()
    total = 0
    with codecs.open(file,encoding='utf-8', errors='ignore') as the_file:
        lines = the_file.read().splitlines()
        for line in lines:
            words = line.split(' ')
            for word in words:
                word = word.lower().strip()
                # print(word)
                word = justWord(word) # Should we really clean?
                # print("cleaned",word)
                if word not in freq.keys():
                    freq[word] = 0
                root.addWord(word)
                freq[word] += 1
                total += 1
    data[lang] = {
        'total_words': total,
        'root': root,
        'word_count': freq
    }

pprint.pprint(data)
build('pride.txt','eng')
pprint.pprint(data)
# build('hindi.txt','hin')
# pprint.pprint(data)