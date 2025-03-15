import argparse
from math import gcd

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def check_fibonacci_gcd(m, n):
    Fm, Fn = fibonacci(m), fibonacci(n)
    gcd_mn = gcd(m, n)
    Fgcd_mn = fibonacci(gcd_mn)
    
    print(f"F({m}) = {Fm}, F({n}) = {Fn}")
    print(f"gcd({m}, {n}) = {gcd_mn}")
    print(f"F(gcd({m}, {n})) = {Fgcd_mn}")
    print(f"gcd(F({m}), F({n})) = {gcd(Fm, Fn)}")
    print("Property holds?", gcd(Fm, Fn) == Fgcd_mn)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Fibonacci GCD property")
    parser.add_argument("-n", type=int, required=True, help="First number")
    parser.add_argument("-m", type=int, required=True, help="Second number")
    args = parser.parse_args()

    check_fibonacci_gcd(args.m, args.n)