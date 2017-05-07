from timeit import default_timer
from ugly_python import run_it

if __name__ == "__main__":
    start = default_timer()
    run_it()
    print('Running time was: {}'.format(default_timer() - start))
