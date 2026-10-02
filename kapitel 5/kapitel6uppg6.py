a=input('Skriv en text och se hur denna magiska kod lyckas ta bort alla mellanslag: ')

a = a.replace(' ', '')
a = a.replace('\t', '')


print(a)