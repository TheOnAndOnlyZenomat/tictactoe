import random
import re       # for regular expressions
import os

# global variables
general = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]    # to know which fields there are
avail = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]      # to know which fields are used
player1 = []                                                        # fields claimed by the player
player2 = []                                                        # fields claimed by the player
player1score = 0                                                    # to know which players turn, value gets increased per turn, player with lower score has turn
player2score = 0
x = "5468654f6e416e644f6e6c795a656e6f6d61742f41647269616e2045696368656c6261756d"

def cellcheck(avail, pos):
    "checks if cell is already in use"
    if avail.count(pos) > 0:
        check = 0
        return check
    else:
        print("Already in use. Try again.")
        check = 1
        return check

def move(avail, player1, player1score, player2, player2score):
    "takes care of the move"
    os.system('clear')
    if player1score == 0 and player2score == 0:
        print("Player1's turn")
        print("====================")
        print(f"Those fields are available: {avail}")
    elif player1score > player2score:
        print("Player2's turn")
        print("====================")
        print(f"Those are the ones you already choose: {player2}")
        print(f"Those fields are available: {avail}")
    elif player2score >= player1score:
        print("Player1's turn")
        print("====================")
        print(f"Those are the ones you already choose: {player1}")
        print(f"Those fields are available: {avail}")
    pos = str(input("On which field do you want to place your mark? "))

    check = cellcheck(avail, pos)
    while check == 1:
        print("Already in use. Try again.")
        pos = str(input("On which field do you want to place your mark? "))
        check = cellcheck(avail, pos)

    if player1score == 0 and player2score == 0:
        player1.append(pos)
        player1score +=1
        avail.remove(pos)
    elif player1score > player2score:
        player2.append(pos)
        player2score +=1
        avail.remove(pos)
    elif player2score >= player1score:
        player1.append(pos)
        player1score +=1
        avail.remove(pos)
    return player1score, player2score

def checkwin(general, avail, player1, player2):
    "checks if one player won"
    # stores the winning combinations in the corresponding variables
    cella = re.compile("a[1-3]")
    cellb = re.compile("b[1-3]")
    cellc = re.compile("c[1-3]")
    cell1 = re.compile("[a-c]1")
    cell2 = re.compile("[a-c]2")
    cell3 = re.compile("[a-c]3")
    # following statement checks if on of the winning combinations are found in one of the lists -> if yes it return the winner, if not it returns "none"
    if set(list(filter(cella.match, avail))).issubset(player1) == True or set(list(filter(cellb.match, avail))).issubset(player1) == True or set(list(filter(cellc.match, avail))).issubset(player1) == True or \
        set(list(filter(cell1.match, avail))).issubset(player1) == True or set(list(filter(cell2.match, avail))).issubset(player1) == True or set(list(filter(cell3.match, avail))).issubset(player1) == True or \
        set(["a1", "b2", "c3"]).issubset(player1) == True or set(["a3", "b2", "c2"]).issubset(player1) == True:
        win = "Player1"
        return win
    elif set(list(filter(cella.match, avail))).issubset(player2) == True or set(list(filter(cellb.match, avail))).issubset(player2) == True or set(list(filter(cellc.match, avail))).issubset(player2) == True or \
        set(list(filter(cell1.match, avail))).issubset(player2) == True or set(list(filter(cell2.match, avail))).issubset(player2) == True or set(list(filter(cell3.match, avail))).issubset(player2) == True or \
        set(["a1", "b2", "c3"]).issubset(player2) == True or set(["a3", "b2", "c2"]).issubset(player2) == True:
        win = "Player2"
        return win

def main(general, avail, player1, player1score, player2, player2score):
    win = checkwin(general, avail, player1, player2)
    while win == None:
        player1score, player2score = move(avail, player1, player1score, player2, player2score)
        win = checkwin(general, avail, player1, player2)

    if win == "Player1":
        print("Player1 won the game")
    elif win == "Player2":
        print("Player2 won the game")

main(general, avail, player1, player1score, player2, player2score)
