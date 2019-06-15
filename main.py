def initGrid():
    # initialize grid
    row = [" "," "," "]
    grid = [row.copy(), row.copy(), row.copy()]
    return grid

def printGrid(grid):
    print(grid[0][0], "|", grid[0][1], "|", grid[0][2])
    print("- + - + -")
    print(grid[1][0], "|", grid[1][1], "|", grid[1][2])
    print("- + - + -")
    print(grid[2][0], "|", grid[2][1], "|", grid[2][2])

# ask user for position to put X
grid = initGrid()
playerX = int(input("What is x position?"))
playerY = int(input("What is y position?"))
grid[playerY][playerX]="X"
printGrid(grid)

# print situation with X

# put 0 somewhere empty

# print situation with 0

# repeat
