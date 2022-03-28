def board(lis):
    print("----------------------------------")
    print(f"|{lis[0]} | {lis[1]} | {lis[2]}|")
    print(f"|{lis[3]} | {lis[4]} | {lis[5]}|")
    print(f"|{lis[6]} | {lis[7]} | {lis[8]}|")
    print("----------------------------------")
def check_draw(lis,draw_num = 0 ,draw=False):
    for i in lis:
        if i.isnumeric():
            draw_num += 1
    if draw_num == 0:
        draw = True
        return draw
def pattern1(increment_win , win , user , lis):
    for i in range(3):
        if lis[i] == user:
            increment_win += 1
            if increment_win == 3:
                win = True
                break
    increment_win = 0
    for i in range(3,6):
        if lis[i] == user:
            increment_win += 1
            if increment_win == 3:
                win = True
                break
    increment_win = 0
    for i in range(6,9):
        if lis[i] == user:
            increment_win += 1
            if increment_win == 3:
                win = True
                break
    increment_win = 0
    return win
def pattern2(increment_win , win , user,lis):
    for i in range(0,9,3):
        if lis[i] == user:
            increment_win += 1
            if increment_win == 3:
                win = True
                break
    increment_win = 0
    for i in range(1,10,3):
        if lis[i] == user:
            increment_win += 1
            if increment_win == 3:
                win = True
                break
    increment_win = 0
    for i in range(2,11,3):
        if lis[i] == user:
            increment_win += 1
            if increment_win == 3:
                win = True
                break
    increment_win = 0
    return win
def diangonal_shape(win, user,lis):
    if ((lis[0] == user) and (lis[4] == user) and (lis[8] == user)):
        win = True
    elif ((lis[2] == user) and (lis[4] == user) and (lis[6] == user)):
        win = True
    return win
##################################################################
##################################################################
def human_game(name, x_o_player, lis , cond = True):
    while cond:
        human_player = input(f"{name} play with {x_o_player} : ")
        if (human_player.isdigit() and int(human_player) <= 9 and int(human_player) != 0):
            if ((lis[int(human_player) - 1] == "O") or (lis[int(human_player) - 1] == 'X')):
                print(f"please {name} play in empty space")
            else:
                human_player_nm = int(human_player)
                lis[human_player_nm-1] = x_o_player.upper()
                cond = False
        else:
            print("please enter a valid number from 1 to 9")
def computer_play(player_o_x,lis,lis2 = [] , choise = 0):
    from random import choice
    for i in lis:
        if i.isnumeric():
            lis2.append(i)
    choise = int(choice(lis2))
    if (lis[choise - 1] == "X" or lis[choise - 1] == "O"):
        computer_play(player_o_x,lis)
    else:
        lis[(choise - 1)] = player_o_x
def gameplay(name1,name2,player1, player2,lis , counter , increment_win = 0 , win = False , draw = False):
    board(lis)
    while counter < 9:
        draw = check_draw(lis)
        if draw:
            print("no one win you Draw ")
            break
        human_game(name1, player1, lis )
        win = pattern1(increment_win , win , player1 ,lis)
        win = pattern2(increment_win , win , player1 ,lis)
        win = diangonal_shape(win, player1 ,lis)
        board(lis)
        if win :
            print(f"{name1} is win ")
            break
        draw = check_draw(lis)
        if draw:
            print("no one win you Draw ")
            break
        human_game(name2, player2, lis)
        win = pattern1(increment_win , win ,player2 ,lis)
        win = pattern2(increment_win , win , player2 ,lis)
        win = diangonal_shape(win, player2 ,lis)
        board(lis)
        if win :
            print(f"{name2} is win ")
            break
        draw = check_draw(lis)
        if draw:
            print("no one win you Draw ")
            break
        counter += 1
def gameplay2(name ,x_o_player, lis ,counter , win = False , draw = False ,increment_win = 0):
    board(lis)
    while counter < 9:
        draw = check_draw(lis)
        if draw:
            print("you draw with computer ")
            break
        while True:
            if x_o_player.lower() == 'x':
                human_game(name,'x',lis)
                board(lis)
                win = pattern1(increment_win , win , 'X',lis)
                win = pattern2(increment_win , win , "X",lis)
                win = diangonal_shape(win, "X",lis)
                if win :
                    print(f"{name} you win")
                    counter = 9 
                    break
                draw = check_draw(lis)
                if draw:
                    print("you draw with computer ")
                    counter = 9
                    break
                print("computer play : .. ")
                computer_play("O",lis)
                board(lis)
                win = pattern1(increment_win , win , "O",lis)
                win = pattern2(increment_win, win , "O",lis)
                win = diangonal_shape(win, "O",lis)
                if win :
                    print(f"hard luck {name} you lose")
                    counter = 9
                    break
                draw = check_draw(lis)
                if draw:
                    counter = 9
                    print("you draw with computer ")
                    break
            elif x_o_player.lower() == 'o':
                print("computer play : .. ")
                computer_play("X",lis)
                board(lis)
                win = pattern1(increment_win , win , "X" , lis)
                win = pattern2(increment_win , win , "X" , lis)
                win = diangonal_shape(win, "X" , lis)
                if win :
                    print(f"hard luck {name} you lose")
                    counter = 9
                    break
                draw = check_draw(lis)
                if draw:
                    print("you draw with computer ")
                    counter = 9
                    break
                human_game(name,'o',lis)
                board(lis)
                win = pattern1(increment_win , win , "O" , lis)
                win = pattern2(increment_win , win , "O" ,lis)
                win = diangonal_shape(win, "O" , lis)
                if win :
                    print(f"{name} you win")
                    counter = 9
                    break
                draw = check_draw(lis)
                if draw:
                    print("you draw with computer ")
                    counter = 9
                    break
def game(name1,name2,player1,player2 = '' , cond = True):
    lis = ['1','2','3','4','5','6','7','8','9']
    if name2 == 'none':
        if player1 == "X":
            gameplay2(name1 ,player1 ,  lis , counter = 0)
        else:
            gameplay2(name1 , player1 , lis , counter = 0)      
    else:
        if player1 == "X":
            player2 = "O"
            gameplay(name1 ,name2 ,player1 , player2 , lis , counter = 0)
        else:
            player2 = "X"
            gameplay(name2,name1 ,player2 , player1 , lis , counter = 0)
def player_x_o(name):
    x_o_player1 = input(f"{name1} what sympole you want to paly with x or o : ")
    if x_o_player1.lower() == 'x':
        return x_o_player1.upper()
    elif x_o_player1.lower() == 'o':
        return x_o_player1.upper()
    else:
        print("please put x or o only")
        player_x_o(name)
def allgame(name1):
    while True:
        resonse = input("if you want to play with computer press c if you want to play with anyone press f and if you wnat to quit press q:")
        if resonse.lower() == 'c':
            x_o_player1 = player_x_o(name1)
            name2 = "none"
            game(name1 , name2 , x_o_player1)
        elif resonse.lower() == 'f':
            name2 = input("put name of second player : ")
            x_o_player1 = player_x_o(name1)
            game(name1 , name2, x_o_player1)
        elif resonse.lower() == 'q':
            print("good bye")
            break
        else:
            print("please press valid value")
name1 = input("put your name : ")        
allgame(name1)
