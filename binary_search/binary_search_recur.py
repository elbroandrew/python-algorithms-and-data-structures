'''рекурсивно'''

def bs_recur(arr, n, start, end):
    # base case
    if start > end:
        return "Not found."

    mid = (start + end) // 2

    if arr[mid] == n:
        return 'Found.'

    if arr[mid] > n:
        # look left part
        return bs_recur(arr, n, start, mid-1)
    elif arr[mid] < n:
        return bs_recur(arr, n, mid+1, end)
        

arr1 = [1,3,5,7,8,9,10,15,22,34,56,67,78,89,100]
x = bs_recur(arr1, 6, 0, len(arr1)-1)
print(x)