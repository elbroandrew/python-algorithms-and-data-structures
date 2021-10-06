def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        no_swaps = True
        for j in range(0, i - 1):
            if arr[j] > arr[j + 1]:
                # SWAP
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                # Check Swaps
                no_swaps = False
            if no_swaps:
                break
    return arr


x = bubble_sort([123, 1, 2, 3, 4, 5, 6, 7, 8, 98])
print(x)
