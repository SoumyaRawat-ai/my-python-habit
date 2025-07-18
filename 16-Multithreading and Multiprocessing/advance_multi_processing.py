### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    return f"Square: {number * number}"

numbers= [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 8,5,6,7,77,74, 3,]
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
        
    for result in results:
        print(result)