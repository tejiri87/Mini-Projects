#FIBONACCI FUNCTION

import numpy as np

def generate_fibonacci(x):
    fibonacci_numbers = [0,1]
    for n in range(2,x):
        next_fibonacci_numbers = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fibonacci_numbers)
    return fibonacci_numbers

np.generate_fibonacci = generate_fibonacci


