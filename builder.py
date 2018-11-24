# coding=utf-8

import codecs
import re
import helpers
from trie import Trie

def build(file, data, lang = 'def') :

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
                    if word not in counts.keys() :
                        counts[word] = 0
                        root.addWord(word)
                    counts[word] += 1
    
    data[lang] = {
        'total_words': sum(counts.values()),
        'root': root,
        'word_count': counts,
        'unique_words': sorted(counts.keys()),
    }

    return data
