import random
import threading
import time

MAX_RANGE = 20

MIN_NUMBER = -30
MAX_NUMBER = 30
NEGATIVE_BUFFER = abs(MIN_NUMBER) if MIN_NUMBER < 0 else 0 


arr = [random.randint(MIN_NUMBER, MAX_NUMBER) for x in range(MAX_RANGE)]
print(arr)

sorted_arr = []


def sleep_sort_step(x):
    time.sleep(NEGATIVE_BUFFER+x)
    print(x)
    sorted_arr.append(x)


def print_arr(arr, sleep_dur):
    time.sleep(sleep_dur)
    print(arr)


for x in arr:
    t = threading.Thread(target=sleep_sort_step, args=(x,))
    t.start()

t = threading.Thread(target=print_arr, args=(sorted_arr, NEGATIVE_BUFFER+max(arr)+1))
t.start()
