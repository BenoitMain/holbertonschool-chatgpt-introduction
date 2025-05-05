#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Compute the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial to compute.

    Returns:
        int: The factorial of n (n!).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the command-line argument, compute its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
