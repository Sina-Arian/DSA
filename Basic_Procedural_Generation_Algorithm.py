import random

width = 100
height = 35

drunk = {
    'wall_countdown' : 900,
    'padding' : 2,
    'x' : int(width // 2),
    'y' : int(height // 2)
}

def getLevelRow():
    return ['#'] * width

level = [getLevelRow() for _ in range(height)]

while drunk['wall_countdown'] >= 0:
    x = drunk['x']
    y = drunk['y']

    if level[y][x] == '#':
        level[y][x] = ' '
        drunk['wall_countdown'] -= 1

    roll = random.randint(1, 4)

    if roll == 1 and x > drunk['padding']: 
        drunk['x'] -= 1
    
    elif roll == 2 and x < width - 1 - drunk['padding']:
        drunk['x'] += 1
    
    elif roll == 3 and y > drunk['padding']:
        drunk['y'] -= 1

    elif roll == 4 and y < height - 1 - drunk['padding']:
        drunk['y'] += 1

for row in level:
    print(''.join(row))