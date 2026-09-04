import math
num1=float(input("Första talet: "))
num2=float(input("Andra talet: "))

print("Välj räknesätt:")
print("1 = +")
print("2 = -")
print("3 = x")
print("4 = /")
#miniräknaren är kass så de fyra räknesätten är det enda som funkar.
sätt=int(input("Räknesätt: "))

if sätt==1:
    print(f"Svaret blir {num1} + {num2} = {num1+num2}")
elif sätt==2:
    print(f"Svaret blir {num1} - {num2} = {num1-num2}")
elif sätt==3:
    print(f"Svaret blir {num1} * {num2} = {num1*num2}")
elif sätt==4:
    print(f"Svaret blir {num1} / {num2} = {num1/num2}")
else:
    print(f"Svaret blir  {num1} upphöjt i två * roten ur {num2} = {num1**2*math.sqrt(num2):.2f}")