kö=[]

for i in range(1, 6):
    namn=input("Lägg till någon i kön: ")
    kö.append(namn)

while True:

    if kö == []:
        print("Nu är kön tom, då blir det rast!")
        break

    print(f"Nu betjänas {kö[0]}")
    
    kö.pop(0)
    
    print(f"Kvar i kön :{kö}")

    fortsätt=input("När du vill fortsätta, tryck enter. ")
    if fortsätt == '':
        continue