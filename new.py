def hangman (word):
    wrong = 0
    stage = ["", 
             "___________      ",
             "|                ",
             "|                ",
             "|      |         ",
             "|      0         ",
             "|     /|\        ",
             "|     / \        "
            ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('welcome to hangman')
    while wrong < len(stage) - 1:
        print('\n')
        msg = '1文字予測してね'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stage[0:e]))
        if '_' not in board:
            print('you win')
            win = True
            break
