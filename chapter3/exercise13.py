import random

class Markov():
    def __init__(self):
        self.words = {}
        self.state = (None, None, None)

    def add(self, word):
        if self.state in self.words:
            self.words[self.state].append(word)
        else:
            self.words[self.state] = [word]
        self._transition(word)

    def _transition(self, next):
        self.state = (self.state[1], self.state[2], next)

    def reset(self):
        self.state = (None, None, None)

    def randomNext(self):
        lst = self.words.get(self.state) # it returns a list
        choice = random.choice(lst)
        self._transition(choice)
        return choice

def makeLower(word:list):
    for i in word:
        i.lower()
    return word

def trainModel():
    inFile = open('vedicName.txt', 'r')
    model = Markov()
    char_obj = [] #its a list of list of characters
    for line in inFile:
        lstOfWords = line.split(', ')
        for w in lstOfWords:
            w = w.lower()
            w_char = []
            for c in w:
                w_char.append(c)
            w_char.append('$')
            char_obj.append(w_char)

    for o in char_obj:
        for c in o:
            model.add(c)

    inFile.close()
    model.reset()
    return model

def generateText(model):
    words = []
    for i in range(10): #number of words
        word = []
        for t in range(10): #maximum length of the each word
            next_char = model.randomNext()
            if next_char == '$':
                words.append(''.join(word))
                break
            else:
                word.append(next_char)

    return words

trained = trainModel()
print(generateText(trained))
