# 水族館の料金の計算する関数

def calc_fee(age, is_monday):
    fee = 2000 # 一般2000円
    #年齢に応じて割引
    if age < 3:
        fee = 0
    elif age< 6:
        fee = 500
    elif age >=60:
        fee = 1500
    if is_monday:
        fee = int(fee * 0.8)
    return fee 

# 関数を利用する

print(calc_fee(2, True))
print(calc_fee(18, False))
print(calc_fee(70, True))
print(calc_fee(20, True))
