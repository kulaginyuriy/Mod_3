x = float(input("Введите начальный вклад: "))
p = float(input("Введите процентную ставку: "))
y = float(input("Введите конечную сумму: "))

years = 0
while x < y:
    x = float(x + x * p / 100)
    print (f"Вклад составляет = :{round(x,2)}") 
    years += 1

print("Количество лет:", years)