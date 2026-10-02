a= ' Erik Andersson 14/03-2714 '

a = a.strip()
i = a.rfind(' ')+1
j = a.find('-')
b = a[i:j]

print(a)
print(i)
print(j)
print(b)