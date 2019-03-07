# class number:
#     def __init__(self, base):
#         self.data = []
#         self.base = base
#
#
#
#
# # modified counting sort
# def counting_sort(arr, cur, base):
#     count_arr = [0 for _ in range(base + 1)]
#     res = [0] * len(arr)
#     for el in arr:
#         count_arr[el] += 1
#     for i in range(1, ar_max + 1):
#         count_arr[i] += count_arr[i - 1]
#     for i in range(len(arr) - 1, -1, -1):
#         res[count_arr[arr[i]] - 1] = arr[i]
#         count_arr[arr[i]] -= 1
#     return res
#
#
# # radix sort, using counting sort
# def radix_sort(arr, base=10):
#     pass