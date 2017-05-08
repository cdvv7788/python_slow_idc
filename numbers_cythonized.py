from timeit import default_timer
from new_ugly_python import run_it_2

if __name__ == "__main__":
    start = default_timer()
    run_it_2()
    print('Running time was: {}'.format(default_timer() - start))
