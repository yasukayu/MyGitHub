

def hangman():
    word_list = ["apple","orange","cherry","grape","peach"]
    import random
    word = word_list[random.randint(0,len(word_list)-1)]
    
    wrong = 0
    stages = ["",
              "____________",
              "|           ",
              "|      |    ",
              "|      〇   ",
              "|    ／|＼  ",
              "|    ／ ＼  ",
              "|           "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想して入力してください。"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ちです")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負けです。正解は{}.".format(word))

                       
hangman()


