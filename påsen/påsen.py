påse=[]

print("Välkommen till påsen! Vad vill du göra?")
while True:
    print("")
    print("[V] Visa innehållet i påsen")
    print("[S] Lägg till något i påsen")
    print("[F] Leta efter en specifik sak i påsen")
    print("[Q] Avsluta programmet")
    print("[D] Ta bort något påsen")
    print("[X] Töm påsen")

    val=input("Ditt val: ").lower()

    if val == "v":
        print("Ok, här är allt som finns i påsen!")
        print(f"{påse}")
        gåvidare = input("Vill du gå vidare? I så fall, tryck enter: ")

        if gåvidare == "":
            continue

    elif val == "s":
        while True:
            läggtill = input("Vad vill du lägga till? ")
            påse.append(läggtill)
            print(f"{läggtill} har lagts till i påsen.")
            
            fortsätta = input("Vill du fortsätta? [j / n]")
            if fortsätta == "j":
                continue
            else:
                break
        


    elif val == "f":
        leta = input("Ok, vad letar du efter? ")
        if leta in påse:
            print(f"Ja, {leta} finns i påsen!")
        else:
            print(f"Nej, {leta} finns inte i påsen.")

    elif val == "q":
        break

    elif val == "d":
        tabort = input("Ok, vad vill du ta bort? ")
        if tabort in påse:
            påse.remove(tabort)
            print(f"{tabort} har blivit borttagen.")
        else:
            print(f"{tabort} finns inte i påsen.")

    elif val == "x":
        påse.clear()
        print("Ok, påsen är tömd.")

    else:
        print("Använd en av alternativen tack.")

print("Ok, tack för att du använde påsen!")