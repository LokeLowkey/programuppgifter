import random

tal=random.randint(1,20)

gissning = 0

while gissning != tal:
    gissning = int(input("Gissa på ett tal mellan 1 och 20: "))

    if gissning < tal:
        print("Får lågt!")
    elif gissning > tal:
        print("För högt!")
    else:
        print("Rätt!")
        
