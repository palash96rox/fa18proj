import operator
import codecs as cd #for hindi

class Trie:
    def __init__(self): #defining structure
        self.dic={}
        self.isEnd=False #initializing with false imp..
        
    def addItem(self,word): #Adding new word to trie
        if len(word)==0: 
            self.isEnd=True #word is completed 
            return
        pivot=word[0] #taking first letter
        word=word[1:] #redefining word for again taking new letter
        if pivot in self.dic: # letter is available in dictionary no need to add new key in the dic.
            self.dic[pivot].addItem(word) #repeating for next letter
        else:
            obj=Trie() #making new object
            self.dic[pivot]=obj #givig key as pivot and value as object with empty dict{} and isend=false item is added
            self.dic[pivot].addItem(word) #repeating for next letter
            
    def findInTrie(self,matchfreq,wordfreq,find=None): #finding in trie
        if self.isEnd==True:
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

def cleanData(n): #cleaning data
    f=(".","!",")","|",",","-","।","(","'")
    if n.endswith(f):
        n=n[:len(n)-1]
##        print(n)
    if n.startswith(f):
        n=n[1:]
    return n

def printTop5(matchfreq): #printing highest frequency words
    matchfreq=sorted(matchfreq.items(), key=operator.itemgetter(1)) #sorting according to value sorted in increasing order accord to values
    num=len(matchfreq)
    for i in range(num-1,num-6,-1):
       try:  #exception handling important as there maybe less than 5 elements in matchfreq dictionary
          print(matchfreq[i][0].rstrip())
          if(i)<=0:
             break
       except:
          print("No match") #matchfreq dic is empty
          break

def English(): #for english
    print("English is selected")
    myobj=Trie() #creating object
    f=open("dict.txt",'r')
    lines=f.read().splitlines()#reading file and removing \n
    for i in lines: #reading words
          i=i.lower().strip()
          j=i.split(" ")
          for k in j:
             k=cleanData(k)
             if k not in wordfreq.keys():
                wordfreq[k]=1
                myobj.addItem(k) #adding unique words in trie
             else:
                wordfreq[k]=wordfreq.get(k)+1
    while(True): #taking multiple inputs
        s=input("Enter-")
        if(s=="#"):
            break
        matchfreq={} #dictionary with matched words and frequency
        s=s.lower()
        myobj.search(s,matchfreq,wordfreq) #searching for word
        printTop5(matchfreq)
        print() 
        

def Hindi(): #for hindi
    print("Hindi is selected")
    l1=[]
    l=[]
    hindiobj=Trie()
    f=cd.open("hindi.txt",encoding='utf-8',mode='r') #reading document
    k=f.read().splitlines() #removing \r\n
    for i in k:
        l1=i.split(" ")
        l.append(l1) #whole document in l list 
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            sabd=l[i][j]
            sabd=cleanData(sabd)
            if sabd not in hindi.keys():
                hindi[sabd]=1
                hindiobj.addItem(sabd) #adding unique words in trie
            else:
                hindi[sabd]=hindi.get(sabd)+1
    while(True):#taking multiple inputs
        s=input("Enter-")
        if(s=="#"):
            break
        matchfreq={} #dictionary with matched words and frequency
        s=s.lower()
        hindiobj.search(s,matchfreq,hindi)
        printTop5(matchfreq)
        print()
    

def initialize(): #get set go
    print("Press 1 for English")
    print("Press 2 for Hindi")
    print("Press # for exit")
    s=int(input("Enter="))
    if(s==1):
        English()
    elif(s==2):
        Hindi()
    else:
        exit
    
wordfreq={} #unique words dictionary with frequency for english
hindi={}    #unique words dictionary with frequency for hindi
initialize()

