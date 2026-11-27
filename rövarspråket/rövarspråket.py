vokaler = "aouåeiyäö"
undantag = "cx "

def översättning(text):
    resultat = ""
    for tecken in text:
        if tecken not in vokaler:
            if tecken in undantag:
                if tecken == "c":
                    resultat += "kok"
                elif tecken == "x":
                    resultat += "koksos"
            resultat += tecken + "o" + tecken.lower() #så att det kan t.ex. bli Kok, inte KoK
        else:
            resultat += tecken

    return resultat

text = input("Skriv din mening här: ")
print(översättning(text))