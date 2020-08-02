from typing import List


def max_heapify(arr, cur):
    """push cur element up heap"""
    left = cur * 2 + 1
    right = cur * 2 + 2
    if left < len(arr) and arr[left] > arr[cur]:
        largest = left
    else:
        largest = cur
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != cur:
        arr[cur], arr[largest] = arr[largest], arr[cur]
        max_heapify(arr, largest)
    return arr


def build_heap(arr: List[int]) -> List[int]:
    """create max heap"""
    for i in range(int(len(arr) / 2) - 1, -1, -1):
        arr = max_heapify(arr, i)
    return arr


def heap_sort(arr: List[int]) -> List[int]:
    arr = build_heap(arr)
    cur_len = len(arr)
    for i in range(len(arr)):
        arr[0], arr[cur_len - 1] = arr[cur_len - 1], arr[0]
        cur_len -= 1
        arr[:cur_len] = max_heapify(arr[:cur_len], 0)
    return arr
