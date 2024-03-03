import sys
import copy
import time

# maze = [
#     [' ', ' ', '#', '#', '#', '#', '#'],
#     ['#', ' ', ' ', ' ', ' ', ' ', '#'],
#     ['#', ' ', '#', '#', '#', '#', '#'],
#     ['#', ' ', ' ', ' ', ' ', ' ', '#'],
#     ['#', ' ', '#', '#', '#', ' ', '#'],
#     ['#', ' ', ' ', ' ', '#', ' ', '#'],
#     ['#', '#', '#', '#', '#', 'E', '#']
# ]

maze = [
    [' ', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', '#', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', 'E', '#']
]

directions = [
    [-1, 0],  # Up
    [1, 0],   # Down
    [0, -1],  # Left
    [0, 1],   # Right
]

def find_end(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'E':
                return (i, j)  # Return the position of 'E'

def clear_terminal():
    # ANSI escape code to clear the terminal screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_maze(maze, path):
    time.sleep(.1)

    tempMaze = copy.deepcopy(maze)  # Create a deep copy of the maze
    for point in path:
        tempMaze[point[0]][point[1]] = "\033[94m@\033[0m"  # Mark the path with "@" symbol in blue

    clear_terminal()  # Clear the terminal screen

    for row in tempMaze:
        print(" ".join(row))  # Print the maze row by row

def find(curr, path, seen, needle, maze):
    
    print_maze(maze, path)

    # if off the map
    if (curr[0] < 0 or curr[0] >= len(maze) or
        curr[1] < 0 or curr[1] >= len(maze[0])):
        return False
    
    # if wall
    if maze[curr[0]][curr[1]] == "#":
        return False
    
    # if the ending point
    if curr == needle: 
        path.append(curr)
        return True

    # if we have seen this point
    if curr in seen: 
        return False
    
    # book keeping
    seen.append(curr)
    path.append(curr)

    # call again in all directions
    for x, y in directions: 
        if find((curr[0] + x, curr[1] + y), path, seen, needle, maze):
            return True
        
    # pop off stack if find returns False
    path.pop()

    # return
    return False

def maze_solver(maze):

    # set up path and seen array
    path = []
    seen = []

    # define start and end
    source = (0, 0)
    needle = find_end(maze)

    # call recursive find
    if find(source, path, seen, needle, maze):
        return path
    
print(maze_solver(maze))
