# coding=utf-8
# TODO move all to a class and access via object

import datetime
import codecs
import re
import helpers
from trie import Trie
from consts import DEFAULT_LANGUAGE

def build(file, data, invalids, lang = DEFAULT_LANGUAGE) :

    start = datetime.datetime.now()

    if data.get(lang):
        root = data[lang]['root']
        sentence_root = data[lang]['sentence_root']
        counts = data[lang]['word_count']
    else:
        root = Trie('root',lang)
        counts = dict()
        sentence_root = Trie(lang)

    print()    
    print('file',file)
    print()
    print('word_root\n',root)
    print('sentence_root\n',sentence_root)

    with codecs.open(file, encoding='utf-8', errors='ignore') as the_file:
        doc = the_file.read()
        lines = doc.splitlines()
        words = []
        unique = []

        for line in lines:
            words = re.split(r'\W+',line)
            for word in words:
                word = word.strip()
                if word not in unique: unique.append(word)


        
        
        # sentences = re.split(r'\. |\.$|\?|\!|\r|\t|;|(  )|(\n)|(\n\n)',re.sub(r'(?!\n$)(\n)', lambda matchobj: ' ', doc))
        # sentences = [sentence for sentence in sentences if sentence and sentence.strip()]

        # for sentence in sentences: sentence_root.add(sentence)


        # for line in lines:
        #     words = re.split('\W+',line)
        #     for word in words:
        #         word = word.strip()
        #         if helpers.isAlphabet(word): # NO need to store nums
        #             word = helpers.justWord(word,tuple(invalids))
        #             if word not in counts.keys() :
        #                 counts[word] = 0
        #                 root.addWord(word)
        #             counts[word] += 1
        # print(sentences)
        # for sentence in sentences:
        # #     # sentence = sentence.strip()
        #     sentence_root.addWord(sentence)
        #     print(sentence)
            

    data[lang] = {
        'total_words': sum(counts.values()),
        'root': root,
        'sentence_root': sentence_root,
        'word_count': counts,
        'unique_words': sorted(counts.keys()),
        'unique_count': len(counts.keys()),
    }

    print('time for read', datetime.datetime.now()-start)
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
        
        with codecs.open('lib/data/'+lang+'_sent', encoding='utf-8', mode='w', errors='ignore') as word_file:
            merged = helpers.merge_lists([data[lang]['unique_words'],words_in_file,])
            for word in merged:
                word_file.write(word+'\n')

# def update_file(root,freq,top100,user):
    # TODO
