pris=float(input("Hur mycket pengar kostar köpet? "))

if pris<500:
    print(f"Kostnad: {pris}")
    print(f"Rabatt: 0%")
    print(f"Att betala: {pris}")
elif 500<=pris<1000:
    print(f"Kostnad: {pris}")
    print(f"Rabatt: 10%")
    print(f"Att betala: {pris*0.9:.2f}")
else:
    print(f"Kostnad: {pris}")
    print(f"Rabatt: 20%")
    print(f"Att betala: {pris*0.8:.2f}")