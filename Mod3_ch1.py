x = float(input("есть столько денег="))
y = float(input("Хочу, чтобы было ="))
p = float( input("%="))
time = y/(x*p/100)
z =((x+(x*p/100))*p/100)

while x < y:
    print (f"Time deposit = :{int(x)}")
    x += z
print(f"Вклад достиг: {y} руб, за {int(time)} года/лет") 


  
