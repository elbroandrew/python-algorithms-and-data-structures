arr1 = [1, 5, 5, 5, 5, 7, 7, 7, 7, 6, ]
# result = [1,5, 5,7, 7,6, 8]



def test3(arr):
    i = 0
    j = 1
    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            j += 1
        else:
            i += 1
            arr[j] = None
            j += 1
    
    return [x for x in arr if x != None]


t = test3(arr1)
print(t)