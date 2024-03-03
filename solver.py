maze = [
    [' ', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', 'E', '#']
]

directions = [
    [-1, 0],  # Up
    [1, 0],   # Down
    [0, -1],  # Left
    [0, 1],   # Right
]

def find(curr, path, seen, needle, maze):
    
    # if off the map
    if (curr[0] < 0 or curr[0] > len(maze[0]) or
        curr[1] < 0 or curr[1] > len(maze)):
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
    needle = (6, 5)

    # call recursive find
    if find(source, path, seen, needle, maze):
        return path
    
print(maze_solver(maze))
