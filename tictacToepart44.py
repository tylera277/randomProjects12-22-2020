# 12/24/2020
# part 4 of making tic-tac toe game
# need to now incorporate the text writer in order to write game board out

import sys

from tictacToepart24 import check

i = 1
car = 0
game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
size = int(input("How large of a board do you want? "))

while i < 9.5:
    # Player 1
    row1,comma1,col1= input("Player 1: Enter your move in row,col form:")


    row1Adjusted = int(row1) - 1
    col1Adjusted = int(col1) - 1


    if game[row1Adjusted][col1Adjusted] == 0:
        game[row1Adjusted][col1Adjusted] = 'X'
        print(game)
        for l in range(size):
            for i in range(size):
                print(" ---",end="")
            print("")

            for j in range(size):
                print("|",game[l][j],end=" ")
            print("", end="")
            print("|")



        for i in range(size):
            print(" ---", end="")
        print("")
        if (check(game))==1:
            sys.exit()
        i += 1
        if i == 6:                              # End of game check
            print("Game over!")
            break
    else:
        print("A piece is already there!")
        continue

    # Player 2

    row2, comma2, col2 = input("Player 2: Enter your move in row,col form:")

    row2Adjusted = int(row2) - 1
    col2Adjusted = int(col2) - 1
    if game[row1Adjusted][col1Adjusted] == 0:
        game[row1Adjusted][col1Adjusted] = 'X'
        print(game)



    if game[row2Adjusted][col2Adjusted] == 0:
        game[row2Adjusted][col2Adjusted] = 'O'
        print(game)
        for m in range(size):
            for n in range(size):
                print(" ---",end="")
            print("")

            for o in range(size):
                print("|",game[m][o],end=" ")
            print("",end="")
            print("|")
        for i in range(size):
            print(" ---", end="")
        print("")
        if (check(game)) ==1:
            sys.exit()

                                            # counter only moves when a new piece is added
    else:
        print("A piece is already there")
        car = 1
        continue