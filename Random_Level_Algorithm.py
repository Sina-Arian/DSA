import random

width = 55
height = 25
wall_percentage = 35

def getBlock():
    if random.randint(1, 100) < wall_percentage:
        return '#'
    return ' '

def generateRow():
    return ['#'] + [getBlock() for i in range(width - 2)] + ['#']

edge = ['#'] * width

level = [edge] + [generateRow() for i in range(height - 2)] + [edge]

for row in level:
    print(''.join(row))