def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(0, i - 1):
            if arr[j] > arr[j + 1]:
                # SWAP
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


x = bubble_sort([123, -534, 435, 65, 234, 12, 12, -54, 0, 98, 1])
print(x)
