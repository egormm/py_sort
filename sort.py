from timeit import default_timer as timer

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

fout = open('output.txt', 'w')
fout.write('algorithm\tsmall arr\tbig int\tsorted\tresorted\tbig arr\n')
for func in array_sort:
    print(func.__name__)
    fin = open('input.txt', 'r')
    n = int(fin.readline())
    time_arr = []
    for i in range(n):
        cur_arr = list(map(int, fin.readline().split(" ")))
        start_time = timer()
        sorted_arr = func(cur_arr)
        delta_time = timer() - start_time
        time_arr += [delta_time]
    fout.write(func.__name__+'{:10f}{:10f}{:10f}{:10f}{:10f}\n'.format(*time_arr))
    fin.close()
fout.close()