from GameAI import Gaming
import pickle

inFile = open(r'C:\Users\Sina\Documents\DSA_Zelle\saveGame.bin', 'rb')

myGame = Gaming(pickle.load(inFile))
myGame.start()
