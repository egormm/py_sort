from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """add elements to sorted previous slice"""
    for i in range(1, len(arr)):
        cur_elem = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur_elem:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur_elem
    return arr
