from timeit import default_timer

n = 10000000000

def run_it():
    output = 'a'*n

if __name__ == "__main__":
    start = default_timer()
    run_it()
    print('Running time was: {}'.format(default_timer() - start))
