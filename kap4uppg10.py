lösenord="fel"
försök=3
while lösenord != "Python123":
    lösenord=str(input("Skriv lösenord: "))
    försök-=1
    print(f"Fel! {försök} försök kvar.")
    if försök==0:
        print("Self destruct command activated. Starting countdown...")
        försök==3
        break

if lösenord=="Python123":
    print("Rätt lösenord! Startar...")
