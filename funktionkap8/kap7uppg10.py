def hämta_betyg(poäng):
    if poäng >= 25:
        return "Godkänd"
    else:
        return "Underkänd"
    
print(f"Elev 1: {hämta_betyg(24)}")
print(f"Elev 2: {hämta_betyg(200)}")
print(f"Elev 3: {hämta_betyg(25)}")