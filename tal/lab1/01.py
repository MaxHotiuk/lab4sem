import random

a = []
b = []
n, m = 10, 15
for i in range(n):
    a.append(random.randint(1, 10))
for i in range(m):
    b.append(random.randint(1, 10))

a.sort()
b.sort()
print(a)
print(b)
c = []

while len(b) != 0 or len(a) != 0:
    if len(a) == 0:
        var = b[0]
    elif len(b) == 0:
        var = a[0]
    else:
        var = min(a[0], b[0])
    if len(a) != 0 and a[0] == var:
        c.append(a[0])
        a.pop(0)
    elif len(b) != 0 and b[0] == var:
        c.append(b[0])
        b.pop(0)

print(c)