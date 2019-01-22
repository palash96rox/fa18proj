class Trie:
    def __init__(self):
        self.dic = {}
        self.isEnd = False

    def addWord(self, word):
        if len(word) == 0:
            self.isEnd = True
            return
        key = word[0] # Maybe use just the unicode and not the actual character?
        if key not in self.dic:
            self.dic[key] = Trie()
        self.dic[key].addWord(word[1:])
            
    def findInTrie(self, matchfreq, wordfreq, find=None): #finding in trie
        if self.isEnd == True:
##            print(find) #word is found
            matchfreq[find]=wordfreq.get(find) #getting frequency of words from main wordlist
        for i in self.dic.keys():
            self.dic[i].findInTrie(matchfreq,wordfreq,find+i) #finding word
            
    
    def search(self,word,matchfreq,wordfreq,find=""): #searching till the user input and passing it to search
        if(len(word)>0):
            pivot=word[0]
            word=word[1:]
            if pivot in self.dic: #checking user input in trie 
                find=find+pivot #changing find till end of user input
                self.dic[pivot].search(word,matchfreq,wordfreq,find) #checking user input in trie
            else:
                return
        else: # when whole user input is found 
            for i in self.dic.keys():
                self.dic[i].findInTrie(matchfreq,wordfreq,find+i) #go to search in trie for each available key in dic
