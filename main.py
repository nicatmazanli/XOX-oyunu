import os
import time

### XOX taxtalarimiz
# Bu array esas arrayin bir kopyasidi oyun bitdikde biz esas taxtayi bununla yeniliyeceyik
xox_array1 = ["1", "2", "3",
              "4", "5", "6",
              "7", "8", "9"]
# Bu da esas arrayimizdi
xox_array = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
# Oyuncilarimiz
players = ["X", "O"]
n = 0
m = True
# Oyuncularin Skorlari
score_X = 0
score_Y = 0


def xox_printer():
    # Ekrana bu formada bir yazi cixardacaq
    # 1 | 2 | 3
    # 4 | 5 | 6
    # 7 | 8 | 9
    print(xox_array[0] + " | " + xox_array[1] + " | " + xox_array[2])
    print(xox_array[3] + " | " + xox_array[4] + " | " + xox_array[5])
    print(xox_array[6] + " | " + xox_array[7] + " | " + xox_array[8])


def xox_start(m, n, score_X, score_Y, xox_array1):
    while m:
        xox_printer()
        print("<----------- SCORE ----------->\n",
              "|------ X = ", score_X, "\n",
              "|------ Y = ", score_Y, "\n")
        if (xox_array[0] == xox_array[1] == xox_array[2] == "X") or (
                xox_array[3] == xox_array[4] == xox_array[5] == "X") or (
                xox_array[6] == xox_array[7] == xox_array[8] == "X") or (
                xox_array[0] == xox_array[4] == xox_array[8] == "X") or (
                xox_array[2] == xox_array[4] == xox_array[6] == "X") or (
                xox_array[0] == xox_array[3] == xox_array[6] == "X") or (
                xox_array[1] == xox_array[4] == xox_array[7] == "X") or (
                xox_array[2] == xox_array[5] == xox_array[8] == "X"):
            print("Winner is player X !!!!")
            for i in range(0, 9):
                xox_array[i] = xox_array1[i]
            score_X += 1
            n = 0
            continue
        elif (xox_array[0] == xox_array[1] == xox_array[2] == "O") or (
                xox_array[3] == xox_array[4] == xox_array[5] == "O") or (
                xox_array[6] == xox_array[7] == xox_array[8] == "O") or (
                xox_array[0] == xox_array[4] == xox_array[8] == "O") or (
                xox_array[2] == xox_array[4] == xox_array[6] == "O") or (
                xox_array[0] == xox_array[3] == xox_array[6] == "O") or (
                xox_array[1] == xox_array[4] == xox_array[7] == "O") or (
                xox_array[2] == xox_array[5] == xox_array[8] == "O"):
            print("Winner is player O !!!!")
            score_Y += 1
            n = 0
            for i in range(0, 9):
                xox_array[i] = xox_array1[i]
            continue
        print("Player Turn " + players[n])
        number = str(input(" Number (1-9) ::> "))
        if number in xox_array:
            b = xox_array.index(number)
            xox_array.pop(b)
            xox_array.insert(b, players[n])
            if n == 0:
                n = 1
            else:
                n = 0
        elif number == "exit":
            print("OK... Quitting")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            quit()
        else:
            print("Please enter another value")
            time.sleep(1.4)


def starting(m, n, score_X, score_Y):
    os.system("cls")
    for i in range(0, 4):
        print(".", end="")
        time.sleep(0.5)
    os.system("cls")
    print("\nOK...", end="")
    time.sleep(0.8)
    print("Setting up something...")
    time.sleep(1.5)
    print("Hello", end=" ")
    time.sleep(1.5)
    print("...", end=" ")
    time.sleep(2)
    print("Player", end=" ")
    time.sleep(2)
    print("What is your name? ")

    name = input(" > ")

    print("Hmmmmm......")
    time.sleep(3)
    print("Are you want to play game? (y/n)")
    pl_gm_an = input()
    if pl_gm_an == "y":
        print("OK...")
    else:
        print("Ok... I am quitting in 5 seconds")
        for i in range(5, 0):
            print(i)
            time.sleep(1)
        quit()

    print("I think you and your friend want to plat XOX game... Right (enter) ")
    input()

    print("And this is game start in 3")
    time.sleep(1)
    print("game start in 2")
    time.sleep(1)
    print("game start in 1")
    time.sleep(1)
    xox_start(m, n, score_X, score_Y, xox_array1)


### Oyunu baslat
xox_start(m, n, score_X, score_Y, xox_array1)

### Hekayə qatmaq istəyirsənsə sonrakı sətri kommentdən çıxart
# starting(m,n,score_X,score_Y,xox_array1)
