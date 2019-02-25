cells = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
counter = 1

def printGame():
    for c in range(9):
        if c % 3 == 0:
            row = '| '
        row += cells[c] + " | "
        if c == 2 or c == 5 or c == 8:
            print(row)


def makeMove(row, col):
    global cells
    index = int(row) * 3 + int(col)
    cells[index] = 'x' if counter % 2 != 0 else 'o'

def isLegalMove(row, col):
    global cells
    index = int(row) * 3 + int(col)
    return cells[index] == ' '

def isWinner(move):
    global cells
    return (cells[0] == cells[1] == cells[2]== move) or (cells[3] == cells[4] == cells[5]== move) or (cells[6] == cells[7] == cells[8]== move) or (cells[0] == cells[3] == cells[6]== move) or (cells[1] == cells[4] == cells[7]== move) or (cells[2] == cells[5] == cells[8]== move) or (cells[0] == cells[4] == cells[8]== move) or (cells[2] == cells[4] == cells[6]== move)

inputs = ["1,1","2,0","0,0","0,1","0,2","1,2","2,2","2,1","1,0"]
# inputs = "0,1"
# inputs = "1,1"
print("Before game:")
while counter < len(inputs):
    printGame()
    print("\nEnter move: row,col")

    move = 'x' if counter % 2 != 0 else 'o'
    player = str(2 - counter % 2)
    while True:
        row = inputs[counter-1].split(',')[0]
        col = inputs[counter-1].split(',')[1]
        print("Simulating Player " + player + " places " +  move + " on: " +row+","+col)

        if isLegalMove(row, col):
            makeMove(row, col)
            break
        else:
            print("Sorry, that cell is taken.")

    # Since each player is alternating, we know it takes at least 3 moves for PL1 to win after PL2 marks 2
    if counter >= 5 and isWinner(move):
        printGame()
        print("\nThe winner is " + move + " (Player " + player +")")
        break

    counter += 1

if not isWinner(move):
    print("No winner. It's a draw")

