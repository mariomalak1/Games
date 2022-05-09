"""
Number scrabble Game
Created by : Mario Malak Alabd ; id : 20210313
Created in 2022 / 2 /21
"""
###
# game functions here
###
# function to check that the input from user is played before or not by return true if it has accepet the value that the user send
def Check_list(index , lis , counter = 0):
    for i in lis:
        if i == index:
            return True
        else:
            counter += 1
    if counter == len(lis):
        return False
# after check that the user play real integer and not in list of the game before i make the function that remove the number that the user choose it and change it by letter X
def Digit_Change(number ,lis , index = 0):
    for i in lis:
        if i == number:
        	lis[index] = "X"
        	break
        index += 1
###
# function that check that any user is win or not , as i send to it list , and this list is has the numbers that the user choose it and if it has more than three elements the function try to found if the sum of any three elements of this is equal to 15 or not , if it equal to 15 it will return true
def Game_Win(lis):
    if len(lis) < 3:
        return False
    else:
        for i in lis:
            for j in lis:
                for m in lis:
                    if (((i + m + j) == 15) and (i != j) and (i != m) and (j != m)):
                        return True
###
# this function make check if the game end with draw or not, if the list of game ended and was hasn't have any numbers in it and all elements is X , and no one win , so this is draw condition
def Game_Draw(lis ,counter = 0):
    for i in lis:
        if i.isdigit():
            counter += 1
    if counter == 0:
        return True
    else:
        return False
###
# this function of all game that i call all functions here
def Game_play(lis , user1 = 0 , user2 = 0 , lis1 = [] , lis2 = []):
    # print the list of game to user
    print("Enter Number From 1 To 9")
    print("---------------------------------------------")
    print(lis)
    print("---------------------------------------------")
    # this is infinity loop and it will be ended when any player is win or at draw condition  
    while True:
        # make infinity loop to make the user 1 always paly if he play false value 
        while True:
            try:
                # user 1 play and check that he play a real integer 
                user1 = int(input("User 1 Play : "))
                # send the number that the user choose it to function check list to show if the number played before or not
                if Check_list(str(user1) , lis):
                    Digit_Change(str(user1) ,lis)
                    lis1.append(int(user1))
                    # print the list of this user 1 numbers and print list of the game
                    print("user 1 numbers =" , lis1)
                    print("---------------------------------------------")
                    print(lis)
                    print("---------------------------------------------")
                    break
                else:
                    # if user 1 play number has been played will show this message
                    print("Please Enter Number Not Used Before , Try Again")
            except ValueError:
                # if user 1 enter non integer value will show this message
                print("Please Enter Number From 1 To 9 ")
        # to check if user 1 is win or not
        if Game_Win(lis1):
            print(f"User 1 Is Win ")
            break
        # to check that is draw or not
        if Game_Draw(lis):
            print("No One Win You Draw ")
            break
        # make infinity loop to make the user 1 always paly if he play false value 
        while True:
            try:
                # user 2 play and check that he play a real integer 
                user2 = int(input("User 2 Play : "))
                # send the number that the user choose it to function check list to show if the number played before or not
                if Check_list(str(user2) , lis):
                    Digit_Change(str(user2) ,lis)
                    lis2.append(int(user2))
                    # print the list of this user 2 numbers and print list of the game
                    print("user 2 numbers =" , lis2)
                    print("---------------------------------------------")
                    print(lis)
                    print("---------------------------------------------")
                    break
                else:
                    # if user 2 play number has been played will show this message
                    print("Please Enter Number Not Used Before , Try Again")
            except ValueError:
                # if user 2 enter non integer value will show this message
                print("Please Enter Number From 1 To 9 ")
        # to check if user 2 is win or not
        if Game_Win(lis2):
            print(f"User 2 Is Win ")
            break
        # to check that is draw or not
        if Game_Draw(lis):
            print("No One Win You Draw ")
            break
# main function 
if __name__ == "__main__":
    # list of the game
    lis = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # function of all game
    Game_play(lis)
