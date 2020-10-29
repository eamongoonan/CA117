from sys import argv
from math import sqrt

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    N = int(argv[1]) + 1
    m_of = "Multiples of"
    print(m_of, "3:", [i for i in range(1, N) if i % 3 == 0])
    print(m_of, "3 squared:", [i ** 2 for i in range(3, N, 3)])
    print(m_of, "4 doubled:", [i * 2 for i in range(1, N) if i % 4 == 0])
    print(m_of, "3 or 4:", [i for i in range(1, N) if i % 3 == 0 or i % 4 == 0])
    print(m_of, "3 and 4:", [i for i in range(1, N) if i % 3 == 0 and i % 4 == 0])
    print(m_of, "3 replaced:", ["X" if i % 3 == 0 else i for i in range(1, N)])
    print("Primes:", [i for i in range(2, N) if is_prime(i)])

if (__name__ == "__main__"):
    main()
