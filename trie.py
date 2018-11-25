class Trie:

    def __init__(self):
        self.dic = {}
        self.isEnd = False
        self.weight = 1

    def __str__(self):
        stri = ''
        stri += 'Probability from previous: ' + str(self.weight)
        stri += '\nNextNode: '
        stri += str(sorted(self.dic))
        stri += '\n\n\n'
        return stri

    def addWord(self, word):
        if len(word) == 0:
            self.isEnd = True
            return
        key = ord(word[0])
        if key not in self.dic:
            self.dic[key] = Trie()
        self.dic[key].addWord(word[1:])

    def num_count(self, word):
        if len(word) == 0:
            return self.count
        key = ord(word[0])
        if key not in self.dic:
            return 0
        return self.dic[key].num_count(word[1:])

    def exists(self, word):
        if len(word) == 0:
            return self.isEnd
        key = ord(word[0])
        if key not in self.dic:
            return False
        return self.dic[key].num_count(word[1:])

    def calculate_weight(self, value, total):
        # 0.5*(frequency of word) + 0.5*(probabilty of that pattern)
        word, count = value

        prob = count/total

        node = self
        weight = 0
        for letter in word:
            key = ord(letter)
            weight += node.dic[key]
            node = node.dic[key]
        weight = weight/len(word)

        val = 0.5*prob + 0.5*weight

        return (word,val)

