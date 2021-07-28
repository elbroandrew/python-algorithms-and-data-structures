'''только для сортированного массива'''

# iterative solution

arr = [1,3,5,7,8,9,10,15,22,34,56,67,78,89,100]

def bs_iter(arr, num):
    
    start = 0
    end = len(arr)-1

    while(start <= end):
        mid = (start + end) // 2
        if num == arr[mid]:
            return 'Element found'
        if num < arr[mid]:
            end = mid - 1
        if num > arr[mid]:
            start = mid + 1

    return 'Element not found'

x = bs_iter(arr, 15)
print(x)