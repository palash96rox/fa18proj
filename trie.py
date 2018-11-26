# coding=utf-8

class Trie:

    def __init__(self, lang='eng'):
        self.isEnd = False
        self.count_letter_in_word = 0
        self.count_typing_pattern = 0
        self.dic = self.create_dict(lang.lower())


    def create_dict(self,lang):
        # Src https://www.periodni.com/unicode_utf-8_encoding.html
        dic = dict()
        # DEFAULT - ENGLISH
        files = ['eng']
        if 'hin' in lang:
            files.append('hin')
        if 'fr' in lang:
            files.append('fr')
        if 'ita' in lang:
            files.append('ita')
        if 'de' in lang:
            files.append('de')
        if 'es' in lang.lower():
            files.append('es')
        if 'gr' in lang.lower():
            files.append('gr')
        for file in files:
            with open('lib/lang/chars/'+file) as the_file:
                chars = the_file.read().splitlines()
                for char in chars: dic[ord(char)] = None
        return dic

    def __str__(self):
        stri = ''
        stri += 'letter: ' + str(self.count_letter_in_word) + '\n'
        stri += 'typing: ' + str(self.count_typing_pattern) + '\n'
        stri += '\nNextNode: '
        stri += str(sorted(self.dic))
        stri += '\n\n'
        return stri

    def __dict__(self):
        dic = dict()
        # node = self
        # while(node != )
        # for key in node.keys():
        # TODO
        return dic

    def addWord(self, word):
        if len(word) == 0:
            self.isEnd = True
            return
        key = ord(word[0])
        if self.dic.get(key):
            self.dic[key] = Trie()
        self.dic[key].count_letter_in_word += 1
        self.dic[key].addWord(word[1:])

    def exists(self, word):
        if len(word) == 0:
            return True
        key = ord(word[0])
        if key not in self.dic:
            return False
        return self.dic[key].num_count(word[1:])

    def calculate_weight(self, value, total):
        # 0.2*(frequency of word) + 0.3*() + 0.5*(typing_style)
        word, count = value

        freq = count/total

        node = self
        word_weight = 0
        for letter in word:
            key = ord(letter)
            word_weight += node.dic[key].count_letter_in_word
            node = node.dic[key]
        word_weight = word_weight/len(word)

        typing_weight = 0
        while(word != 0):
            node = self
            if not node.exists(word): break

        val = 0.2*freq + 0.3*word_weight + 0.5*typing_weight

        return (value[0],val)

    # Get the total number of times the letters are typed in that order for a word
    def get_counts(self,node,word,sum=0):
        if len(word) == 0: return sum
        key = ord(word[0])
        node = node.dic[key]
        sum += node.count_letter_in_word
        print(chr(key),':',node.count_letter_in_word)
        return self.get_counts(node,word[1:],sum)

    # Called at every word completion
    def update_word_count(self,node,word):
        if len(word) == 0: return node
        key = ord(word[0])
        node = node.dic[key]
        node.count += 1
        return self.update_counts(node,word[1:])

    # Called 
    def update_typing_pattern(self,node,typed):
        if len(typed) == 0: return node
        key = ord(typed[0])
        node = node.dic[key]
        node.count_typing_pattern += 1
        return update_senetence_count(node,sentence[1:])