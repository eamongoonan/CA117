def fibonacci(n):
    if 1 < n:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 1
