import chapter2_cardADT

def printAll():
    for suit in 'cdhs':
        for rank in range(1,14):
            myCard = chapter2_cardADT.create(rank, suit)
            print(chapter2_cardADT.toString(myCard))

if __name__ == '__main__':
    printAll()