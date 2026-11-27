import random
spelare = 100
herman = 100

def visa_status(spelare, herman):
    print(f"Spelare: {spelare} | Herman: {herman}")

def visa_meny():
    print("\n1. Svärdshugg |15 - 20 hp|")
    print("2. Eldklot |0 - 35 hp|")
    print("3. Potion |+15 - 25 hp")
    print("4. Häxblandning |-15 - 45 hp")

def spelarens_drag(val, spelare, herman):
    if val == 1:
        skada = random.randint(15, 20)
        herman -= skada
        print(f"Herman blir svärdhuggen och tar {skada} skada!")
    elif val == 2:
        skada = random.randint(0, 35)
        herman -= skada
        print(f"Herman blir träffad av ett eldklot och tar {skada} skada!")
    elif val == 3:
        heal = random.randint(15, 25)
        spelare += heal
        print(f"Riddaren dricker en potion och healar {heal} skada!")
        if spelare > 100: 
            spelare = 100
    elif val == 4:
        heal = random.randint(-15, 50)
        spelare += heal
        print(f"Riddaren dricker häxblandningen och healar {heal} skada!")
        if spelare > 100:
            spelare = 100
        
    else:
        print("Ogiltigt val")
    
    return spelare, herman
        
    
def monstrets_drag(spelare):
    herman_skada = random.randint(10, 25)
    spelare -= herman_skada
    print(f"Riddaren blir klöst av Herman och tar {herman_skada} skada!")
    return spelare

while True:
    visa_status(spelare, herman)

    visa_meny()

    val = int(input("Vad väljer du att göra? "))
    spelare, herman = spelarens_drag(val, spelare, herman)

    if herman > 0:
        spelare = monstrets_drag(spelare)
        if spelare <= 0:
            print("Riddaren förlorade.")
            break
    else:
        print("Herman är dräpt!")
        break