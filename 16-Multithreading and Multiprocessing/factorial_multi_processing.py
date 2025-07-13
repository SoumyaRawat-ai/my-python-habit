import multiprocessing
import math
import sys
import time

# Increase the maximum number of digit for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial of given number

def computer_factorial(number):
    print(f"computing factorial of {number}")
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == "__main__":
    number = [5000, 6000, 700, 8000]
    
    start_time = time.time()
    
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, number)
        
    end_time = time.time()
    
    print(f'Result: {results}')
    print(f'Time taken {end_time - start_time} seconds')