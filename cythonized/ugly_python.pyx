from timeit import default_timer

cdef int n
n = 10000000000  # Still ugly, but can handle 10

def run_it():
    cdef int i
    cdef str output
    output = ''
    for i in range(0, n):
        output = output + 'a'
