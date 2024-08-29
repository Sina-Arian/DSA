def pathToExit(TupleCoord, maze, prevCells= []):
    y, x = TupleCoord
    if y > len(maze.maze)-1 or x > len(maze.maze[0])-1:
        return False
    
    print(y,x)
    if maze.maze[y][x] == 'E':
        return True
    if (maze.maze[y][x] == '*') or ((y,x) in prevCells):
        return False
    prevCells.append((y,x))
    if pathToExit((y+1, x), maze, prevCells):
        return True
    if pathToExit((y, x+1), maze, prevCells):
        return True
    if pathToExit((y-1, x), maze, prevCells):
        return True
    if pathToExit((y, x-1), maze, prevCells):
        return True
    
    prevCells.remove((y,x))
    return False


class Maze:
    def __init__(self, file):
        inFile = open(file, 'r')
        self.maze = []
        for line in inFile:
            line = list(line)
            if line[-1] == '\n':
                line = line[:-1]
            self.maze.append(line)
        self.masireTaInja = []

    def __str__(self):
        out = ''
        for line in self.maze:
            out += f'{line}\n'
        return out


def main():
    myMaze = Maze(r'C:\Users\Sina\Documents\DSA_Zelle\chapter6\maze.txt')
    res = pathToExit((0,0), myMaze)
    if res == True:
        print("I'm out")
    else:
        print("No Way Out")
main()