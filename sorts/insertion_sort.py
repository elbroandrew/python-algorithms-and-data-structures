arr = [3, 5, 12, 4, 7, 8, 2, 1, 9, 0]


for i in range(1, len(arr)):
    cur = arr[i]
    j = i - 1
    while(j >= 0 and arr[j] > cur):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = cur

print(arr)