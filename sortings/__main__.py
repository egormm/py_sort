from timeit import default_timer as timer
import csv

from sortings.bubble import bubble_sort_r, bubble_sort_f
from sortings.shuffle import shuffle_sort
from sortings.selection import selection_sort
from sortings.insertion import insertion_sort
from sortings.counting import counting_sort_r, counting_sort_o, counting_sort_s
from sortings.heap import heap_sort
from sortings.radix import radix_sort
from sortings.quick import quick_sort

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

def main():
    with open("../output.csv", 'w') as fout:
        writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['algorithm', 'small arr', 'big int', 'sorted', 'resorted', 'big arr'])
        with open('../input.txt', 'r') as fin:
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


if __name__ == '__main__':
    main()
