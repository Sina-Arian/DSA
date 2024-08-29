from random import random, randint

def customerGenerator(filename, maxItem, totalTicks, arrivalInterval):
    out = open(filename, 'w')
    for i in range(totalTicks):
        if random() < 1.0/arrivalInterval:
            items = randint(0, maxItem)
            print('{i} {items}'.format(**locals()), file= out)
    out.close()

customerGenerator('customerList.txt', 25, 3*60*60, 20)
