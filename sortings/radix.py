from typing import List
from math import log


class Number:
    """
    Special class to iterate numerals in number
    """

    def __init__(self, n, base):
        self._base = base
        self.n = n

    def __getitem__(self, key):
        assert key >= 0, "key >= 0"
        return (self.n // self._base ** key) % self._base


def counting_sort(num_arr, cur, base):
    """
    Modified counting sort

    :param num_arr: array of Number-s
    :param cur: current index of numeral
    :param base: base of radix sort
    :return: sorted array of Number-s
    """

    count_arr = [0 for _ in range(base + 1)]
    res = [None] * len(num_arr)
    for el in num_arr:
        count_arr[el[cur]] += 1
    for i in range(1, base + 1):
        count_arr[i] += count_arr[i - 1]
    for i in range(len(num_arr) - 1, -1, -1):
        res[count_arr[num_arr[i][cur]] - 1] = num_arr[i]
        count_arr[num_arr[i][cur]] -= 1
    return res


def radix_sort(arr, base=10):
    """
    Radix sort, using modified counting sort

    :param arr: array of int-s
    :param base: base of radix sort
    :return: sorted array of int-s
    """

    num_arr = [Number(n, base) for n in arr]

    cur = 0
    while base ** cur <= max(arr):
        num_arr = counting_sort(num_arr, cur, base)
        cur += 1

    for i in range(len(arr)):
        arr[i] = num_arr[i].n
    return arr
