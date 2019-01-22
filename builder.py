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
        
        sentences = re.split(r'\. |\.$|\?|\!|\r|\t|;|(  )|(\n)|(\n\n)',re.sub(r'(?!\n$)(\n)', lambda matchobj: ' ', doc))
        sentences = [sentence for sentence in sentences if sentence and sentence.strip()]

        for sentence in sentences: 
            sentence_root.add(sentence)
            


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
            

data = dict()

# Word cleaner
def justWord(word) :
    # print('received--',word)
    invalid = ('.','!','(',')','[',']','{','}','|',',','-','।','\'','_',';',':','\"','”','“',' ')
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
        'total_words': sum(counts.values()),
        'root': root,
        'sentence_root': sentence_root,
        'word_count': counts,
        'unique_words': sorted(counts.keys()),
        'unique_count': len(counts.keys()),
    }

pprint.pprint(data)
build('pride.txt','eng')
pprint.pprint(data)
build('hindi.txt','hin')
pprint.pprint(data)
