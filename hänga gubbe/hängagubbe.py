ordet=input('Vilket ord ska din motståndare gissa på? ').lower()
gissningar=[' ']
felgissningar=0
maxgissningar=6
gubben = [
r"""
 ♥ ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥
      O
     /|\
     / \
""",
r"""
      
      O
     /|\
     / \
"""
]

while felgissningar < maxgissningar:
    display = ''
    for bokstav in ordet:
        if bokstav in gissningar:
            display+=bokstav+''
        else:
            display+='_'

    print(gubben[felgissningar])

    print('ord: ' + display)

    if '_' not in display:
        print('Du vann!')
        print(f'Hela ordet är: {ordet}')
        break
    
    print(f'Gissningar hittills: {gissningar}')

    gissning=input('Din gissning: ').lower()

    if len(gissning) != 1 or not gissning.isalpha():
        print('Du vet reglerna dumskalle')
        continue

    if gissning in gissningar:
        print('Den bokstaven har du redan gissat på!')
        continue

    gissningar.append(gissning)

    if gissning in ordet:
        print('Rätt gissat!')
    else:
        felgissningar+=1
        print('Du gissade fel noob')

else:
    print(gubben[maxgissningar])
    print('Du förlorade noob')
    print(f'Ordet var: {ordet}')