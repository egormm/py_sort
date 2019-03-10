def counting_sort_s(arr):
    """stupid counting sort"""
    ar_max = max(arr)
    ar_min = min(arr)
    count_arr = [0 for _ in range(ar_max - ar_min + 1)]
    for el in arr:
        count_arr[el - ar_min] += 1
    arr[:] = []
    for i in range(ar_min, ar_max + 1):
        arr += [i] * count_arr[i - ar_min]
    return arr


def counting_sort_r(arr):
    """regular counting sort"""
    ar_max = max(arr)
    count_arr = [0 for _ in range(ar_max + 1)]
    res = [0] * len(arr)
    for el in arr:
        count_arr[el] += 1
    for i in range(1, ar_max + 1):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        res[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    return res


def counting_sort_o(arr):
    """counting sort with small optimisation - count slice from min to max"""
    ar_min = min(arr)
    ar_max = max(arr)
    count_arr = [0] * (ar_max - ar_min + 1)
    res = [0] * len(arr)
    for el in arr:
        count_arr[el - ar_min] += 1
    for i in range(1, ar_max - ar_min + 1):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        res[count_arr[arr[i] - ar_min] - 1] = arr[i]
        count_arr[arr[i] - ar_min] -= 1
    return res
