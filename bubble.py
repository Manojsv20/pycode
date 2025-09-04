def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def bsort(arr, n):
    for i in range(n-1):
        flag = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:   # compare current and next
                swap(arr, j, j+1)   # pass indices, not values
                flag = 1
        if flag == 0:  # no swaps → already sorted
            break

# Example
list1 = [16, 15, 6, 8, 5]
n = len(list1)
bsort(list1, n)
print(list1)