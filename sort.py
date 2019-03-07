from timeit import default_timer as timer
import csv

from bubble_sort import bubble_sort_r, bubble_sort_f
from shuffle_sort import shuffle_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from counting_sort import counting_sort_r, counting_sort_o, counting_sort_s
from heap_sort import heap_sort

array_sort = [
    bubble_sort_r,
    bubble_sort_f,
    shuffle_sort,
    selection_sort,
    insertion_sort,
    counting_sort_o,
    counting_sort_r,
    counting_sort_s,
    heap_sort
]

# for func in array_sort:
#     fout = open(func.__name__ + '.txt', 'w')
#     fin = open('input.txt', 'r')
#     n = int(fin.readline())
#     for i in range(n):
#         cur_arr = list(map(int, fin.readline().split(" ")))
#         fout.write(str(i + 1) + '. Original array:\n')
#         fout.write(' '.join(map(str, cur_arr)) + '\n')
#         fout.write('Sorted array:\n')
#         start_time = timer()
#         sorted_arr = func(cur_arr)
#         delta_time = timer() - start_time
#         fout.write(' '.join(map(str, sorted_arr)) + '\n')
#         fout.write("Sorting time = " + '{:f3}'.format(delta_time*60000) + '\n\n')
#     fout.close()
#     fin.close()

# fout = open('output.csv', 'w')
# fout.write('algorithm\tsmall arr\tbig int\tsorted\tresorted\tbig arr\n')
# for func in array_sort:
#     with open('input.txt', 'r') as fin:
#         n = int(fin.readline())
#         time_arr = []
#         for i in range(n):
#             cur_arr = list(map(int, fin.readline().split(" ")))
#             start_time = timer()
#             sorted_arr = func(cur_arr)
#             delta_time = timer() - start_time
#             time_arr += [delta_time]
#         fout.write(func.__name__+'{:10f}{:10f}{:10f}{:10f}{:10f}\n'.format(*time_arr))
# fout.close()

with open("output.csv", 'w') as fout:
    writer = csv.writer(fout, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['algorithm', 'small arr', 'big int', 'sorted', 'resorted', 'big arr'])
    with open('input.txt', 'r') as fin:
        [n], *arrays = list(map(lambda x: list(map(int, x.strip('\n').split(' '))), fin.readlines()))
    for func in array_sort:
        time_arr = []
        for i in range(n):
            start_time = timer()
            sorted_arr = func(arrays[i])
            delta_time = round(timer() - start_time, 10)
            time_arr += [delta_time]
        writer.writerow([func.__name__]+time_arr)