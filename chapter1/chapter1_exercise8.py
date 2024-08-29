from random import randint

'''8.Design and implement a quiz program. The program should ...'''

class Quiz:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0
        self.answer_question = []
        self.state_list = []
        self.data = {}

        with open('chapter1_stats.txt', 'r') as inFile:
            list_file = inFile.readlines()
            for item in list_file:
                state, capital = item.split(':')
                capital = capital.split('\n')
                self.data[state] = capital[0]
                self.state_list.append(state)


    def start(self):
        n = randint(0, 51)
        a = input('Enter the capital of {0}: '.format( self.state_list[n] ))
        while a != '':
            a = a.lower()
            t = (a, self.state_list[n])
            self.answer_question.append(t)
            n = randint(0, 50)
            a = input('Enter the capital of {0}: '.format( self.state_list[n] ))


    def evaluation(self):
        for E in self.answer_question:
            ans, que = E
            if self.data[que] == ans:
                self.correct += 1
            else:
                self.incorrect += 1
    

    def result(self):
        print('Correct answers are', self.correct)
        print('Incorrect answers are', self.incorrect)


test1 = Quiz()
test1.start()
test1.evaluation()
test1.result()