"""
Prime Number Checker — Optimized
Suggested time: 12–15 minutes
Problem
Given an integer N, determine if it is a prime number. Then, print the sum of all prime numbers from 2 up to N.
Examples
Input: N = 10
10 is not prime.
Primes up to 10: [2, 3, 5, 7]
Sum of primes: 17
Input: N = 7
7 is prime.
Primes up to 7: [2, 3, 5, 7]
Sum of primes: 17
Constraints
You may not use range() to iterate from 2 to N directly for the primality check. You must use a while loop.
To check if a number is prime, stop checking divisors at its square root (use i * i <= num without importing math).
Do not use sum().
Do not import libraries.
Do not hardcode the answer.
What This Tests: Loops, math logic (square root optimization), nested loops, accumulators, and conditionals.

"""

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if not num % i:
            return False
        i += 2

    return True

def primeNumChecker(num):
    if isPrime(num):
        prime_status = "prime."
    else:
        prime_status = "not prime."
    primes = []
    primes_sum = 0
    i = 2
    while i <= num:
        if isPrime(i):
            primes.append(i)
            primes_sum += i
        i += 1
    return(f"{num} is {prime_status}\n"
           f"Primes up to {num}: {primes}\n"
           f"Sum of primes: {primes_sum}"
    )

        
num = int(input("Enter ineger to check if it is a prime: "))
print(primeNumChecker(num))
