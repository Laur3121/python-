import random

win = 0
draw = 0

#3会勝負

for i in range(3):
    print("じゃんけん" + str(i + 1) + "回目")
    print("> 0:グー、1:チョキ、2:パー")
    #コンピューターの手を決める
    com = random.randint(0,2)
    #自分の手を入力
    you = int(input("あなたの手は？"))
    #ジャンケンの結果を判定
    n = (com - you + 3) % 3
    if n == 0:
        print("あいこ")
        draw = draw +1
    elif n == 1:
        print("勝ち！！！！！")
        win = win + 1
    else:
        print("負け")
    print("---")

# 最終的な対戦結果の表示
print("結果=3戦" + str(win) + "勝" + str(draw) + "引き分け")