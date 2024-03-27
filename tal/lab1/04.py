a = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 5, 5, 7, 9]


i = j = 0
bl = True
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        print("No")
        bl = False
        break

if j == len(b):
    print("Yes")
elif bl:
    print("No")
    