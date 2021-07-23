"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def least_common_multiple(divisors):
  n = m = max(divisors)
  divisors = divisors[1:]

  while True:
    n += m
    for div in divisors:
      if n % div != 0:
        break
    else:
      # Runs if we exit the for loop without `break`-ing
      return n

if __name__ == "__main__":
  from time import time

  divisors = sorted(list(range(1, 21)), reverse=True)

  start = time()
  print(least_common_multiple(divisors))
  print(f"Sorted time: {time() - start:.3f}")
