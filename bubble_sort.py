# regular bubble sort
def bubble_sort_r(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# bubble sort with flag
def bubble_sort_f(arr):
    for i in range(len(arr) - 1):
        sorted_flag = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = True
        if not sorted_flag:
            # means that we didn't do any swap-operations,
            # therefore array is already sorted
            break
    return arr