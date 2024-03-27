matrix = [
    [1, 2, 3, 4, 6, 8, 8],
    [2, 3, 4, 6, 7, 8, 9]
]
target = int(input("Enter a number: "))
m, n = len(matrix), len(matrix[0])
i, j = 0, n - 1 
iff = False
while i < m and j >= 0:
    if matrix[i][j] == target:
        iff = True
        break
    elif matrix[i][j] < target:
        i += 1 
    else:
        j -= 1

if iff:
    print("Yes")
else: print("No")