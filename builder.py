# coding=utf-8
# TODO move all to a class and access via object

import codecs
import re
import helpers
from trie import Trie

def build(file, data, invalids, lang = 'def') :
    if data.get(lang):
        root = data[lang]['root']
        counts = data[lang]['word_count']
    else:
        root = Trie()
        counts = dict()

    with codecs.open(file, encoding='utf-8', errors='ignore') as the_file:
        lines = the_file.read().splitlines()
        for line in lines:
            words = re.split('\W+',line)
            for word in words:
                word = word.lower().strip()
                if helpers.isAlphabet(word): # NO need to store nums
                    word = helpers.justWord(word,tuple(invalids))
                    if word not in counts.keys() :
                        counts[word] = 0
                        root.addWord(word)
                    counts[word] += 1
    
    data[lang] = {
        'total_words': sum(counts.values()),
        'root': root,
        'word_count': counts,
        'unique_words': sorted(counts.keys()),
        'unique_count': len(counts.keys()),
    }

    return data

def def_trie_builder(library={},invalids=[]):
    data = dict()
    for lang in library.keys():
        for book in library[lang]:
            data = build(book,data,invalids,lang)
    return data

def trie_builder(books=[],invalids=[]):
    data = dict()
    for book in books:
        data = build(book,data,invalids,'session')
    return data['session']['root'],data['session']['word_count']

def update_files(data,):
    for lang in data.keys():
        words_in_file = []
        
        try:
            with codecs.open('lib/data/'+lang, encoding='utf-8', mode='r+', errors='ignore') as word_file:
                words_in_file = word_file.read().split('\n')
        except:
            words_in_file = []
        
        with codecs.open('lib/data/'+lang, encoding='utf-8', mode='w', errors='ignore') as word_file:
            merged = helpers.merge_lists([data[lang]['unique_words'],words_in_file,])
            for word in merged:
                word_file.write(word+'\n')
