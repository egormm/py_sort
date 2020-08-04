import matplotlib.pyplot as plt
from sortings import bubble
from time import time
from random import randint


def sort1(arr):
    start = time()
    bubble.bubble_sort_f(arr)
    return time()-start

plt.ion()
x=[]
y=[]
for i in range(10, 1000, 100):
    x.append(i)
    y.append(sort1([randint(-500, 500) for _ in range(i)]))
    plt.plot(x, y)
    plt.pause(0.3)
