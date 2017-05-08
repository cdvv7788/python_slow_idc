from timeit import default_timer

n = 100000000  # Only 8...10 take too long

def run_it():
    output = ''
    for i in range(0, n):
        output = output + 'a'

if __name__ == "__main__":
    start = default_timer()
    run_it()
    print('Running time was: {}'.format(default_timer() - start))
