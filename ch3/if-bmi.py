#体重身長の入力

w = float(input("体重は何kg?"))
h = float(input("身長は何cm?"))

bmi = w/ (h / 100) ** 2
print("BMI=" + str(bmi))

#BMIの値で判定
if bmi <18.5:
    print("痩せ型")
elif 18.5 <= bmi < 25:
    print("普通体重")
elif bmi >= 25:
    print("肥満")      