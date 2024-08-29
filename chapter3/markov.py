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
        lst = self.words.get(self.state)
        choice = random.choice(lst)
        self._transition(choice)
        return choice

def trainModel():
    inFile = open('storm.txt', 'r')
    model = Markov()
    for line in inFile:
        lstOfWords = line.split(' ')
        for w in lstOfWords:
            model.add(w)
    inFile.close()
    model.add(None)
    model.reset()
    return model

def generateText(model, n):
    words = []
    for i in range(n):
        w = model.randomNext()
        if w == None: break
        words.append(w)
    res = " ".join(words)
    return res

trained = trainModel()
print(generateText(trained, 1000))
