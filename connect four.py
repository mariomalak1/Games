# functions of game
#to show borad
def borad(lis):
    print(f"| {lis[0]} |")
    print(f"| {lis[1]} |")
    print(f"| {lis[2]} |")
    print(f"| {lis[3]} |")
    print(f"| {lis[4]} |")
    print(f"| {lis[5]} |")
    print("|   1    2    3    4    5    6    7   |")
# to check that the column is fill or not 
def check_symbol(lis , user , counter = 0):
    for i in lis:
        if (((i[user - 1]) == "X") or (((i[user - 1]) == "O"))):
            pass
        else:
            counter +=1
    if counter != 0:
        return True
    else:
        return False
# to put the symbol in a specific in specific column 
def put_symbol(lis , user , symbol):
    for i in lis:
        if lis[5][user-1] == "_":
            lis[5][user-1] = symbol
            break
        elif lis[4][user-1] == "_":
            lis[4][user-1] = symbol
            break
        elif lis[3][user-1] == "_":
            lis[3][user-1] = symbol
            break
        elif lis[2][user-1] == "_":
            lis[2][user-1] = symbol
            break
        elif lis[1][user-1] == "_":
            lis[1][user-1] = symbol
            break
        elif lis[0][user-1] == "_":
            lis[0][user-1] = symbol
            break
def pattern1_raw(lis , symbol , counter = 0):
    for row in lis:
        for element in row:
            if element == symbol:
                if counter > 3:
                    counter = 0
                    break
                else:
                    if row[counter + 1] == symbol:
                        if row[counter + 2] == symbol:
                            if row [counter + 3] == symbol:
                                return True
            counter += 1
        counter = 0
def pattern2_column(lis, symbol , counter_element = 0 , counter_column = 0):
    for row in lis:
        for element in row:
            while counter_column <= 2:
                if lis[5 - counter_column][counter_element] == symbol:
                    if lis[4 - counter_column][counter_element] == symbol:
                        if lis[3 - counter_column ][counter_element] == symbol:
                            if lis[2 - counter_column ][counter_element] == symbol:
                                return True
                counter_column += 1
            counter_column = 0
            counter_element += 1
        counter_element = 0
def pattern3_diagonal_left(lis, symbol , counter_row = 0 , counter_element = 0 , counter = 0):
    lis.reverse()
    for row in lis:
        for element in row:
            if ((counter_element < 4) and (counter_row < 3)):
                if element == symbol:
                    for i in range(4):
                        if lis[counter_row + i][counter_element + i] == symbol:
                            counter += 1
                    if counter == 4:
                        lis.reverse()
                        return True
                    else:
                        counter = 0
            else:
                counter_element = 0
                break
            counter_element += 1
        counter_row += 1
    lis.reverse()            
def pattern3_diagonal_right(lis, symbol , counter_row = 0 , counter_element = 0 , counter = 0):
    lis.reverse()
    for row in lis:
        for element in row:
            if((counter_element >= 3) and (counter_element < 7) and (counter_row < 3)):
                if element == symbol:
                    for i in range(4):
                        if lis[counter_row + i][counter_element - i] == symbol:
                            counter += 1
                    if counter == 4:
                        lis.reverse()
                        return True
                    else:
                        counter = 0
            else:
                if (counter_element > 6):
                    counter_element = 0
            counter_element += 1
        counter_row += 1
    lis.reverse()
def draw(lis , counter = 0):
    for i in lis:
        for j in i:
            if j == '_':
                counter += 1
    if counter == 0:
        return True  
def Game(lis , user1 = 0 , user2 = 0):
    while True:
        borad(lis)
        while True:
            try:
                user1 = int(input("user 1 play : "))
                if user1 in range(1,8):
                    if check_symbol(lis , user1):
                        put_symbol(lis , user1 , "X")
                        break
                    else:
                        print("please play in empty column ")
                else:
                    print("please enter a number from 1 to 7 only ")
            except ValueError:
                print("please enter a number ")
        if pattern1_raw(lis, "X"):
            borad(lis)
            print("user 1 is win ")
            break
        if pattern2_column(lis, "X"):
            borad(lis)
            print("user 1 win ")
            break
        if pattern3_diagonal_left(lis, "X"):
            borad(lis)
            print("user 1 win ")
            break
        if pattern3_diagonal_right(lis, "X"):
            borad(lis)
            print("user 1 win ")
            break
        if draw(lis):
            borad(lis)
            print("no one won, you draw ")
            break
        borad(lis)
        while True:
            try:
                user2 = int(input("user 2 play : "))
                if user2 in range(1,8):
                    if check_symbol(lis , user2):
                        put_symbol(lis , user2 , "O")
                        break
                    else:
                        print("please play in empty column ")
                else:
                    print("please enter a number from 1 to 7 only ")
            except ValueError:
                print("please enter a number ")
        if pattern1_raw(lis, "O"):
            borad(lis)
            print("user 2 is win ")
            break            
        if pattern2_column(lis, "O"):
            borad(lis)
            print("user 2 is win ")
            break
        if pattern3_diagonal_left(lis, "O"):
            borad(lis)
            print("user 2 win ")
            break
        if pattern3_diagonal_right(lis, "O"):
            borad(lis)
            print("user 2 win ")
            break
        if draw(lis):
            borad(lis)
            print("no one won, you draw ")
            break
if __name__ == "__main__":    
    lis = [['_', '_', '_', '_', '_', '_' , '_'], ['_', '_', '_', '_', '_', '_' , '_'], ['_', '_', '_', '_', '_', '_' , '_'], ['_', '_', '_', '_', '_', '_' , '_'], ['_', '_', '_', '_', '_', '_' , '_'], ['_', '_', '_', '_', '_', '_' , '_']]
    Game(lis)
