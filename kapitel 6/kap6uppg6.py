import random

listan=[]

for i in range(1, 101):
    listan.append(random.randint(1,1000))

listan.sort()

print(listan)

print("Maxvärdet i listan är ", listan[-1], " och minvärdet är", listan[0])

medelvärde=(sum(listan)/100)

print("Medelvärdet på talen är ", round(medelvärde))