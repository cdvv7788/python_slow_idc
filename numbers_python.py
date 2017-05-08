from timeit import default_timer

n = 100000000

def run_it():
    output = 0
    for i in range(0, n):
        output += i
        if output >= 1000:
            output = 0

if __name__ == "__main__":
    start = default_timer()
    run_it()
    print('Running time was: {}'.format(default_timer() - start))
