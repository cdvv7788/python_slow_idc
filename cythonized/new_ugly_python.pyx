from timeit import default_timer
n = 100000000


def run_it():
    output = 'a'*n

def run_it_2():
    cdef int output
    cdef int i
    output = 0
    for i in range(0, n):
        output += i
        if output >= 1000:
            output = 0
