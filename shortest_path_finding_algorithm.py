import time

LevelWidth = 20
LevelHeight = 7

level = [
    list('####################'),
    list('#X    #####      ###'),
    list('## ##       #### ###'),
    list('## #### # #####   ##'),
    list('##   ## #   ##  # ##'),
    list('####    ###    ## X#'),
    list('####################')
    ]

def getNextMove(x, y):
    return {
        'left': [x-1,y],
        'right': [x+1,y],
        'up': [x, y-1],
        'down': [x, y+1]
    }.values()

def getShortestPath(level, startCordinate, endCoordinate):
    searchPath = [[startCordinate]]
    visitedCoordinates = [startCordinate]

    while searchPath != []:
        currPath = searchPath.pop(0)
        currCoordinate = currPath[-1]

        currX, currY = currCoordinate

        if currCoordinate == endCoordinate:
            return currPath
        
        for nextCoordinate in getNextMove(currX, currY):
            nextX, nextY = nextCoordinate

            if nextX < 0 or nextX >= LevelWidth:
                continue

            if nextY < 0 or nextY >= LevelHeight:
                continue

            if nextCoordinate in visitedCoordinates:
                continue
            
            if level[nextX][nextY] == '#':
                continue

            searchPath.append(currPath + [nextCoordinate])
            visitedCoordinates += [nextCoordinate]

shortestPath = getShortestPath(level, [1,1], [18,5])

for coordinate in shortestPath:
    x, y = coordinate
    level[x][y] = '.'

    for row in level:
        print(''.join(row))
    
    print('')
    time.sleep(0.25)
