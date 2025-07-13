from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"


numbers = [1, 2, 3, 4, 5,3,4, 5,5 ,5,4, 4, 4,4,4,4,2,4,43,3,4,3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)
    
for result in results:
    print(result)