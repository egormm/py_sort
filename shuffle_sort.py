#bidirectional bubble sort
def shuffle_sort(arr):
    for i in range(int(len(arr)/2)):
        sorted_flag = False
        for j in range(i, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted_flag = True
        for j in range(len(arr) - i - 2, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                sorted_flag = True
        if not sorted_flag:
            # means that we didn't do any swap-operations,
            # therefore array is already sorted
            break
    return arr