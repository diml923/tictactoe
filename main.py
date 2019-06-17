import random

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
    print(grid[2][0], "|", grid[2][1], "|", grid[2][2],"\n\n")

#return true or false if the winner won or not
def Winner(gri):
    return ((gri[0][0]==gri[1][1]==gri[2][2]) or #diagonal
            (gri[0][0]==gri[0][1]==gri[0][2]) or #first row
            (gri[1][0]==gri[1][1]==gri[1][2]) or #second row
            (gri[2][0]==gri[2][1]==gri[2][2]) or #third row
            (gri[0][0]==gri[1][0]==gri[2][0]) or #first column
            (gri[0][1]==gri[1][1]==gri[2][1]) or #second column
            (gri[0][2]==gri[1][2]==gri[2][2]) or #third column
            (gri[2][0]==gri[1][1]==gri[0][2]) )    # diagonal



# ask user for position to put X
grid = initGrid()

playerX = int(input("What is x position?"))
playerY = int(input("What is y position?"))
grid[playerY][playerX]="X"

# print situation with X

printGrid(grid)

# put 0 somewhere empty

while True:
    comX = random.randrange(0,3)
    comY = random.randrange(0,3)
    if (grid[comY][comX]==" "): break
grid[comY][comX]="0"
printGrid(grid)


# repeat1

playerX = int(input("What is x position?"))
playerY = int(input("What is y position?"))
grid[playerY][playerX]="X"
printGrid(grid)

while True:
    comX = random.randrange(0,3)
    comY = random.randrange(0,3)
    if (grid[comY][comX]==" "): break
grid[comY][comX]="0"
printGrid(grid)


# repeat2

playerX = int(input("What is x position?"))
playerY = int(input("What is y position?"))
grid[playerY][playerX]="X"
printGrid(grid)

while True:
    comX = random.randrange(0,3)
    comY = random.randrange(0,3)
    if (grid[comY][comX]==" "): break
grid[comY][comX]="0"
printGrid(grid)

if Winner(grid) :
     print("you won")
else :
     print("tie! ")
