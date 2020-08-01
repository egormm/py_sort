from timeit import default_timer as timer
import csv

from bubble_sort import bubble_sort_r, bubble_sort_f
from shuffle_sort import shuffle_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from counting_sort import counting_sort_r, counting_sort_o, counting_sort_s
from heap_sort import heap_sort
from radix_sort import radix_sort
from quick_sort import quick_sort

array_sort = [
    bubble_sort_r,
    bubble_sort_f,
    shuffle_sort,
    selection_sort,
    insertion_sort,
    counting_sort_o,
    counting_sort_r,
    counting_sort_s,
    heap_sort,
    radix_sort,
    quick_sort
]


with open("output.csv", 'w') as fout:
    writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['algorithm', 'small arr', 'big int', 'sorted', 'resorted', 'big arr'])
    with open('input.txt', 'r') as fin:
        [n], *arrays = list(map(lambda x: list(map(int, x.strip('\n').split(' '))), fin.readlines()))
    for func in array_sort:
        time_arr = []
        for i in range(n):
            true_sorted_arr = sorted(arrays[i])

            start_time = timer()
            sorted_arr = func(arrays[i][:])
            delta_time = round(timer() - start_time, 10)

            assert sorted_arr == true_sorted_arr, "NOT SORTED, with {}, \n[{}]\n[{}]" \
                .format(func.__name__, ', '.join(map(str, sorted_arr)), ', '.join(map(str, true_sorted_arr)))

            time_arr += [delta_time]
        writer.writerow([func.__name__] + time_arr)
