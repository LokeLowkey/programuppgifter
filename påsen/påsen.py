påse=[]

print("Välkommen till påsen! Vad vill du göra?")
while True:
    print("")
    print("[V] Visa innehållet i påsen")
    print("[S] Lägg till något i påsen")
    print("[F] Leta efter en specifik sak i påsen")
    print("[D] Ta bort något påsen")
    print("[X] Töm påsen")
    print("[Q] Avsluta programmet")

    val=input("Ditt val: ").lower()

    if val == "v":
        if len(påse) == 0:
            print("Påsen verkar vara tom. Prova att lägga till något!")
            continue
        else:
            while True:
                print("Här är allt som finns i påsen!")
                print(f"{påse}")
                gåvidare = input("Vill du gå vidare? I så fall, tryck enter: ")

                if gåvidare == "nej jag vill inte":
                    print("Ok då fjant")
                    continue
                else:
                    break

    elif val == "s":
        while True:
            läggtill = input("Vad vill du lägga till? ")
            påse.append(läggtill)
            print(f"{läggtill} har lagts till i påsen.")
            
            fortsätta = input("Vill du fortsätta? [j / n] ")
            if fortsätta == "j":
                continue
            else:
                break
        


    elif val == "f":
        if len(påse) == 0:
            print("Påsen verkar vara tom. Prova att lägga till något!")
            continue
        else:
            while True:
                leta = input("Ok, vad letar du efter? ")
                antal = påse.count(leta)
                if antal > 1:
                    print(f"Ja, {antal} st {leta} finns i påsen!")
                    break
                elif antal == 1:
                    print(f"Ja, {leta} finns i påsen!")
                    break
                else:
                    print(f"Nej, {leta} finns inte i påsen.")
                    break

    elif val == "q":
        break

    elif val == "d":
        if len(påse) == 0:
            print("Påsen verkar vara tom. Prova att lägga till något!")
            continue
        else:
            while True:
                tabort = input("Ok, vad vill du ta bort? ")
                antal_2 = påse.count(tabort)
                if antal_2 > 1:
                    hurmånga = int(input(f"Det verkar finnas flera {tabort} i påsen. Hur många vill du ta bort? "))
                    borttagna = min(hurmånga, antal_2)
                    for i in range(borttagna):
                        påse.remove(tabort)
                    print(f"Ok, {borttagna} st {tabort} har blivit borttagen.")
                    break
                elif antal_2 == 1:
                    påse.remove(tabort)
                    print(f"Ok, {tabort} har blivit borttagen.")
                    break
                else:
                    print(f"{tabort} finns inte i påsen.")
                    break

    elif val == "x":
        if len(påse) == 0:
            print("Påsen verkar vara tom. Prova att lägga till något!")
            continue
        else:
            påse.clear()
            print("Ok, påsen är tömd.")

    else:
        print("Använd en av alternativen tack.")

print("Ok, tack för att du använde påsen!")