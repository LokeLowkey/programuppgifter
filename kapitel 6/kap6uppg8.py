# kontantkort, lägsta pris
namn = []
pris = []
while True:
    s = input('namn och pris för ett kort: ')
    if s=='':
        break
    före, mellan, efter = s.rpartition(' ')
    namn.append(före)
    pris.append(float(efter))
m = min(pris)
k = pris.index(m)
print(namn[k] + ' är billigast')
print(f'kostnad: {m:1.2f} kr/mån')
