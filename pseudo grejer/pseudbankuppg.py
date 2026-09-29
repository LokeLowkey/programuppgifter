saldo = 1000

while True:
    print("Välkommen till bankautomaten! Vad vill du göra?")
    val=int(input("Skriv 1 om du vill ta ut pengar, 2 om du vill sätta in pengar och 3 om du vill avsluta: "))
    
    if val == 1:
        withdraw=int(input("Ok! Hur mycket pengar vill du ta ut? "))
        if withdraw <= saldo:
            print("Tar ut pengar...")
            saldo -= withdraw    #alltså saldo = saldo - withdraw
        else:
            print("Du Har inte så mycket pengar!")
    
    elif val == 2:
        deposit=int(input("Ok! Hur mycket pengar vill du sätta in?"))
        print("Sätter in pengar...")
        saldo += deposit

    elif val == 3:
        print("Ok, avslutar...")
        break

    else: 
        print("Skriv 1, 2 eller 3 tack.")

    print(f"Du har {saldo} pengar på ditt bankkonto!")