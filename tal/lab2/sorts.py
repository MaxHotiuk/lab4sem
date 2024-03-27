def counting_sort(input_arr, output_arr, k):
    count = [0] * k

    for element in input_arr:
        count[element] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    for element in reversed(input_arr):
        output_arr[count[element] - 1] = element
        count[element] -= 1

def radix_sort(arr):
    max_val = max(arr)

    output_arr = [0] * len(arr)

    exp = 1
    while max_val / exp > 0:
        counting_sort_for_radix(arr, output_arr, exp, 10)
        arr[:] = output_arr[:]
        exp *= 10

    return arr

def counting_sort_for_radix(input_arr, output_arr, exp, base):
    n = len(input_arr)
    k = base 
    count = [0] * k

    for num in input_arr:
        digit = (num // exp) % base
        count[digit] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        num = input_arr[i]
        digit = (num // exp) % base
        output_arr[count[digit] - 1] = num
        count[digit] -= 1
        i -= 1

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = tree_insert(root.left, val)
    else:
        root.right = tree_insert(root.right, val)
    return root

def inorder_traversal(root):
    result = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
    return result

def tree_decision_sort(arr):
    root = None
    for val in arr:
        root = tree_insert(root, val)
    return inorder_traversal(root)

def main():
    input_arr = [4, 2, 2, 8, 3, 3, 1]
    output_arr = [0] * len(input_arr)
    k = 9
    counting_sort(input_arr, output_arr, k)
    
    print("Sorted array by counting sort:", output_arr)
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_arr = radix_sort(arr)
    print("Sorted array by radix sort using counting sort:", sorted_arr)
    
    unsorted_arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = tree_decision_sort(unsorted_arr)
    print("Sorted array by tree decision sort:", sorted_arr)

if __name__ == "__main__":
    main()