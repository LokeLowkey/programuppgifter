ord=input("Skriv ett ord, så kommer programmet räkna ut om det är en palindrom eller inte: (det funkar inte med mellanslag, jag är dum och lat) ").lower()

ord.replace(" ", "")
ord.replace("\t", "")

ord_bak=ord[::-1]

print(f"{ord}")
print (f"{ord_bak}")

if ord == ord_bak:
    print("Det är en palindrom, wow!")
else:
    print("Det är inte en palindrom")
