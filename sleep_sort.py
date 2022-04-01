import random
import threading
import time

arr = [random.randint(0, 30) for x in range(20)]
print(arr)

sorted_arr = []


def sleep_sort_step(x):
    time.sleep(x)
    print(x)
    sorted_arr.append(x)


def print_arr(arr):
    time.sleep(31)
    print(arr)


for x in arr:
    t = threading.Thread(target=sleep_sort_step, args=(x,))
    t.start()

t = threading.Thread(target=print_arr, args=(sorted_arr,))
t.start()
