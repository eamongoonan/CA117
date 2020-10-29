def factorial(n):
    if 1 < n:
        return n * factorial(n - 1)
    else:
        return 1
