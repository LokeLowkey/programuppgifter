nollista=[]

while True:
    svar=int(input("Lägg till ett heltal: "))

    if svar == 1234567890:
        break

    nollista.append(svar)

print("Ok, här är listan: ")
print(nollista)

negativ = 0

for svar in nollista:
    if svar < 0:
        negativ+=1
    
print("Så här många negativa tal finns i listan: ", negativ)
