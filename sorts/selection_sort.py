
def sel_sort(arr: list):


    for j in range(0, len(arr)):
        min_index = j
        for i in range(j + 1, len(arr)):
            if arr[min_index] > arr[i]:
                min_index = i

        tmp = arr[j]
        arr[j] = arr[min_index]
        arr[min_index] = tmp

    return arr



def main():
    ar = [5, 7, 2, 3, 1, 0, 6, 8]
    res = sel_sort(ar)
    print(res)



if __name__ == '__main__':
    main()