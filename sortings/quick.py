from typing import List
from random import choice


# def decorator(function):
#     def wrapper(arr: List[int]) -> List[int]:
#         function(arr, 0, len(arr)-1)
#     def wrapper(arr, fst, lst):
#         function(arr, fst, lst)
#     return wrapper
#
#
# @decorator
# def quick_sort(arr, fst, lst):
#     if fst >= lst:
#         return
#
#     i, j = fst, lst
#     pivot = arr[randint(fst, lst)]
#
#     while i <= j:
#         while arr[i] < pivot: i += 1
#         while arr[j] > pivot: j -= 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#             i, j = i + 1, j - 1
#     quick_sort(arr, fst, j)
#     quick_sort(arr, i, lst)
#     return arr
# TODO: find out speed of slices, if this way is faster, finish it

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    else:
        q = choice(arr)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in arr:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)
