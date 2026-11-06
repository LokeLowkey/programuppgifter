lista=[]

while True:
    tal=int(input("Lägg till ett tal: "))

    if tal == 1234567890:
        break

    lista.append(tal)

for tal in lista.copy():
    if tal == 0:
        lista.remove(tal)

print("Utan nollor så ser din lista ut så här: ")
print(lista)
