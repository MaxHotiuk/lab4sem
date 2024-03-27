a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 5, 7, 9]
c = [0, 3, 6, 8, 9]

a.sort()
b.sort()
c.sort()
print(a)
print(b)
print(c)

ait = bit = cit = 0
for i in range(len(a) + len(b) + len(c)):
    minmas = min(a[ait], b[bit], c[cit])
    if a[ait] == b[bit] == c[cit]:
        print(a[ait])
        break
    elif a[ait] == minmas:
        ait += 1
    elif b[bit] == minmas:  
        bit += 1
    else: 
        cit += 1