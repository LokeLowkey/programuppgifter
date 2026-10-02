# Leta efter det sista vita tecknet i en text
s = input('Skriv en text: ')
i = 0   # i används som räknare
for c in reversed(s):
    if c == ' ' or c == '\t':
        break
    i = i + 1
if i < len(s): 
    print(f'Sista vita tecknet finns på plats nr {i+1} bakifrån eller framifrån plats nr {len(s)-i}')
else:
    print('Inget vitt tecken')