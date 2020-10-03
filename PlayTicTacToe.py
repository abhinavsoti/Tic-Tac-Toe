import ValidateUserWin


gamelist = []

def playtictactoe(user1, user2):
    val = 'Empty'
    v_dict = {1: '', 2: '', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:''}

    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Please remember to choose the option only between ' + str(options))

    pattern_list = [[' ','|',' ','|',' '],['_','|','_','|','_'],[' ','|',' ','|',' '],['_','|','_','|','_'],[' ','|',' ','|',' '],[' ','|',' ','|',' ']]

    for p in pattern_list:
        print(*p, sep='')

    val1 = '0'
    val2 = 'X'
    user_flag = 1

    for i in range(9):
        if user_flag == 1:
            val = input(user1 + ', Please choose the options between: ' + str(options))
        elif user_flag == 0:
            val = input(user2 + ', Please choose the options between: ' + str(options))

        while val.isdigit() is False:
            print('Sorry, you should choose enter a number than a text')
            val = input('Please choose the options between: ' + str(options))

        val = int(val)

        while val not in options:
            if user_flag == 1:
                val = input(user1 + ', Please choose the options between: ' + str(options))
            elif user_flag == 0:
                val = input(user2 + ', Please choose the options between: ' + str(options))

            if val.isdigit() is False:
                print('Sorry it is not a number. Looks like, you do not want to play!! ENDING the GAME now')
                exit()
            elif val.isdigit() is True:
                val = int(val)

        if user_flag == 1:
            mark = val1
        else:
            mark = val2

        if val == 1 or val == 2 or val == 3:
            if val == 1:
                pattern_list[0][0] = mark
            elif val == 2:
                pattern_list[0][2] = mark
            else:
                pattern_list[0][4] = mark

        if val == 4 or val == 5 or val == 6:
            if val == 4:
                pattern_list[2][0] = mark
            elif val == 5:
                pattern_list[2][2] = mark
            else:
                pattern_list[2][4] = mark

        if val == 7 or val == 8 or val == 9:
            if val == 7:
                pattern_list[4][0] = mark
            elif val == 8:
                pattern_list[4][2] = mark
            else:
                pattern_list[4][4] = mark

        v_dict[val] = mark
        options.remove(val)

        for p in pattern_list:
            print(*p, sep='')

        winner = ValidateUserWin.validatetictactoe(v_dict, mark)

        if winner == 'Winner':
            if user_flag == 1:
                ret_winner = 'Congratulations!! ' + str(user1).upper() + ' is the winner of the Game!! '
                return ret_winner
            elif user_flag == 0:
                ret_winner = 'Congratulations!! ' + str(user2).upper() + ' is the winner of the Game!! '
                return ret_winner

        if user_flag == 1:
            user_flag = 0
        elif user_flag == 0:
            user_flag = 1
