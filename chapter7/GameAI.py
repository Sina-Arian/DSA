from TreeNode import TreeNode
import pickle

'''10. Write a program to play the animal guessing game. Here's a sample output showing how the game ...'''
'''its a simple decision tree'''

class Gaming():
    def __init__(self,  tree = TreeNode('green', TreeNode('dog'), TreeNode('horse')) ):
        self.tree = tree

    def start(self):
        print('''Welcome to the Animal Game!
        You pick an animal, and I will try o guess what it is. You can help me get better
        at the game by giving me more information when i make a mistake
        The more you play, the better i get.
        Now tink of an animal, and i'll try to guess what it is.''')
        playAgain = 'yes'
        node = self.tree
        while playAgain == 'yes':
            answer = input('is it {node.data}? '.format(**locals()))
            assert answer == 'no' or answer == 'yes'
            if answer == 'no':  # promotes left tree
                if self.itsALeaf(node):
                    if answer == 'no':
                        self._learn(node)
                        playAgain = input('Do you want to play again? ')
                        node = self.tree

                    elif answer == 'yes':
                        print("i'm sooooo smart!")
                        playAgain = input('Do you want to play again? ')
                        node = self.tree

                else: #its an interior node
                    node = node.left

            elif answer == 'yes':
                if self.itsALeaf(node):
                    if answer == 'no':
                        self._learn(node)
                        playAgain = input('Do you want to play again? ')
                        node = self.tree

                    elif answer == 'yes':
                        print("i'm sooooo smart!")
                        playAgain = input('Do you want to play again? ')
                        node = self.tree

                else: #its an interior node
                    node = node.right

        print("Thanks for playing!")
        saveFile = open("saveGame.bin", 'wb')
        pickle.dump(node, saveFile)
        saveFile.close()

    def itsALeaf(self, node):
        return (node.left == None) and (node.right == None)
    
    def _learn(self, node):
        print('Rats! help me to learn')
        NewItem = input('Whats your animal? ')
        NewQuestion = input('Please enter a yes/no question that would select between a {NewItem} and {node.data}: '.format(**locals()))
        NewQuestionAnswer = input('Whats the answer? ')
        if NewQuestionAnswer == 'no':
            node.right = TreeNode(node.data)
            node.left = TreeNode(NewItem)
            node.data = NewQuestion

        elif NewQuestionAnswer == 'yes':
            node.right = TreeNode(NewItem)
            node.left = TreeNode(node.data)
            node.data = NewQuestion
            