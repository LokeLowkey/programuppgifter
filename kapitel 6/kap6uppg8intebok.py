lista=[]

for i in range (1, 6):
    ord=input("Lägg till ett ord i listan: ")
    lista.append(ord)

lista.sort()

print(lista)

lista.reverse()

print(lista)
