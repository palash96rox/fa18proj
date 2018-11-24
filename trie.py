class Trie:

    def __init__(self):
        self.dic = {}
        self.isEnd = False
        self.count = 0

    def __str__(self):
        stri = ''
        stri += 'Times appeared: ' + str(self.count)
        stri += '\nNextNode: '
        stri += str(sorted(self.dic))
        stri += '\n\n\n'
        return stri

    def addWord(self, word):
        if len(word) == 0:
            self.isEnd = True
            self.count += 1
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
