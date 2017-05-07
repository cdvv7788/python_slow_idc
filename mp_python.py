from timeit import default_timer
from multiprocessing import Process, Manager
from time import sleep
import operator
import functools

num_threads = 4
n = 10000000000

def mult(start, extra, return_dict):
    """
    Gets the start number and the number of subsequent values
    """
    if extra != -1:
        upper_bound = start + extra
    else:
        upper_bound = n + 1
    values = range(start, upper_bound)
    output = 'a'*(start - upper_bound)
    return_dict[start] = output

def run_it():
    """
    We calculate factorial(n)
    """
    manager = Manager()
    return_dict = manager.dict()
    processes = []
    n_split = n//num_threads
    output = ''
    for i in range(0, num_threads):
        if i == num_threads - 1:
            limit = -1
        else:
            limit = n_split
        p = Process(target=mult, args=(n_split*i + 1, limit, return_dict))
        p.start()
        processes.append(p)
    for i in processes:
        i.join()
    for key, value in return_dict.items():
        output += value


if __name__ == "__main__":
    start = default_timer()
    run_it()
    print('Running time was: {}'.format(default_timer() - start))
