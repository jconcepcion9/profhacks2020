import random

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
abc = random.randrange(1, 10)


print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + "\n" +
"-----------\n" +
" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + "\n" +
"-----------\n" +
" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "\n" )

print(random.randrange(0, 3))

# difficulty = input("select difficulty, acceptable inputs are 1, 2, or 3")
gameover = 0

def nextround():
    x = 100
    y = 100
    while x < 0 or x > 2:
        x = int(input("x coordinate? (0-2)"))
        if x < 0 or x > 2:
            print("input 0-2")
    while y < 0 or y > 2:
        y = int(input("y coordinate? (0-2)"))
        if y < 0 or y > 2:
            print("input 0-2!!!") 

    if grid[x][y] != " ":
        while grid[x][y] != " ":
            print("sorry! theres already something there, try another coordinate")
            x = int(input("x coordinate? (0-2)"))
            y = int(input("y coordinate? (0-2)"))
            while x < 0 or x > 2:
                x = int(input("x coordinate? (0-2)"))
                if x < 0 or x > 2:
                    print("input 0-2")
            while y < 0 or y > 2:
                y = int(input("y coordinate? (0-2)"))
                if y < 0 or y > 2:
                    print("input 0-2")
        grid[x][y] = "O"
    else:
        grid[x][y] = "O" 
    

    while grid[x][y] != " ":
        x = random.randrange(0, 3)
        y = random.randrange(0, 3)

    grid[x][y] = "X" #enemy turn, didnt put difficult yet

    print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + "\n" +
    "-----------\n" +
    " " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + "\n" +
    "-----------\n" +
    " " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "\n" )


    if grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O":
        print("you win")
        gameover = 1
    elif grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O":
        print("you win")
        gameover = 1
    elif grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O":
        print("you win")
        gameover = 1
    elif grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O":
        print("you win")
        gameover = 1
    elif grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O":
        print("you win")
        gameover = 1
    elif grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O":
        print("you win")
        gameover = 1
    elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O":
        print("you win")
        gameover = 1
    elif grid[2][0] == "O" and grid[1][1] == "O" and grid[0][2] == "O":
        print("you win")
        gameover = 1

    elif grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        print("you lose")
        gameover = 1
    elif grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        print("you lose")
        gameover = 1
    elif grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        print("you lose")
        gameover = 1
    elif grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X":
        print("you lose")
        gameover = 1
    elif grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X":
        print("you lose")
        gameover = 1
    elif grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X":
        print("you lose")
        gameover = 1
    elif grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X":
        print("you lose")
        gameover = 1
    elif grid[2][0] == "X" and grid[1][1] == "X" and grid[0][2] == "X":
        print("you lose")
        gameover = 1

    
## todo, for loop until someone wins or there is no space left
for i in range(0,9):
    nextround()
    if gameover == 1:
        sys.exit()



    