### Processes that run in parallel
## CPU -Bound task-tasks that are heavy on CPU usage (e.g., mathematical computation, data processing).

## Parallel execution Multiple core of the cpu

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f'Square of {i} : {i**2}')
        
def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube of {i} : {i**3}')

if __name__ == "__main__":
    ## create 2 process
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)
    t = time.time()

    ## start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)