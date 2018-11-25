import builder
import helpers
from user import User
from exceptions import UserNotFound, EmptyBookList

class App():
    def __init__(self, state=0, root=None, counts=dict(), user=None):
        self.state = state
        self.root = root
        self.counts = counts
        self.user = user
        self.update_stats(self.counts)

    def update_stats(self,counts):
        self.total_all = sum(self.counts.values())
        self.unique = self.counts.keys()
        self.total_unique = len(self.unique)
        top100_words = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:100] # [(word, count),]
        self.top100 = [self.root.calculate_weight(word,self.total_all) for word in self.top100_words] # [(word,weight),]

    def build_trie(self, books=[]):
        if not self.user: raise UserNotFound
        if books == []: raise EmptyBookSet

        invalids = []
        with open(self.user.scripts+'/invalids.txt') as invalid_chars:
            illegals = invalid_chars.read().splitlines()
            for invalid in illegals:
                if helpers.isNum(invalid): invalids.append(chr(invalid))
                else: invalids.append(invalid)
        
        self.root,self.counts = builder.trie_builder(books,invalids)
        self.update_stats(self.counts)

    def suggest(self,typed=''):
        # Return top 10 suggestions in order of highest probability

        suggestions = []
        # Get all words possible from sequence
        matched_freq = [(word,count) for word,count in self.counts.items() if word.startswith(typed)] 
        typed10_words = sorted(matched_freq, key=lambda kv: kv[1], reverse=True)[:10]
        typed10 = [helpers.curr_node(self.root,typed).calculate_weight(word,self.total_all) for word in typed10_words]

        relevant = [item for item in self.top100 if item[0].startswith(typed)]

        suggestions = sorted(relevant+typed10, key=lambda kv: kv[1], reverse=True)[:10]

        return [item[0] for item in suggestions] # return only the words


class AppController():

    # sessions = { 'session_id': {'instance': App(), 'typed_past': '', 'typed_current': '', 'suggestions': []},}
    def __init__(self, sessions=dict()):
        self.sessions = sessions

    def run_terminal(self):
       # Clear the screen
       pass

    def login(self):
        pass

    def start(self):
        self.run_terminal()
    