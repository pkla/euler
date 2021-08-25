"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def num_collatz_terms(n: int) -> int:
    count = 1
    while True:
        if n == 1:
            return count
        elif n % 2:
            n = 3*n + 1
        else:
            n = n // 2
        count += 1


def euler_14():
    max_terms = 1
    max_n = 1
    for n in range(2, 1000000):
        num_terms = num_collatz_terms(n)
        if num_terms > max_terms:
            max_terms = num_terms
            max_n = n

    return max_n


if __name__ == "__main__":
    print(euler_14())

    #for term in num_collatz_terms(13):
    #    print(term, end=', ')

    #print(num_collatz_terms(13))