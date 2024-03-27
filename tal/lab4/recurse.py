def f1(x1, x2, x3, x4):
    return x1 * (x2 + x3) + x2 * x4

def g2(x):
    return x

def h2(x, y, z):
    return z + 1

def f2(x, y):
    if y == 0:
        return g2(x)
    else:
        return h2(x, y-1, f2(x, y-1))
    
def g3(x):
    return 0

def h3(x, y, z):
    return x + z

def f3(x, y):
    if y == 0:
        return g3(x)
    else:
        return h3(x, y-1, f3(x, y-1))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

print(f1(2, 3, 4, 5))  # Вивід: 20
print(f2(5, 3))  # Вивід: 8
print(f3(5, 3))  # Вивід: 15
unsorted_list = [5, 2, 8, 1, 9, 3]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)  # Вивід: [1, 2, 3, 5, 8, 9]
print(fibonacci(10))  # Вивід: 55
print(fibonacci_iterative(10))  # Вивід: 55
