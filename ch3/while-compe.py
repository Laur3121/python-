# ライブラリを使うことを宣言
import random , time

# 変数を初期化
a=0
b=0
goal = 20

# ユーザーから入力を得る
user = input("aとbどっちの亀が勝つと思いますか？")

#競争開始
print("競争開始")
# a,bのどちらもがゴールについていない間、ランダムな値を足し続ける。

while (a < goal) and (b < goal):
    print("---")
    a = a+ random.randint(1 ,6)
    b = b+ random.randint(1 ,6)

    print("a:" +">" * a + "@")
    print("b:" +">" * b + "@")

#勝者判定
