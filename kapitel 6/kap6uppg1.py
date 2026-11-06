antal=int(input("Hur många tal vill du ha med i talföljden? "))

k=3
tal_nu=2

talföljd=[]

for _ in range (antal):
    talföljd.append(tal_nu)
    tal_nu*=k

print(f"{talföljd}")