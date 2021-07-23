"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n):
  if n < 2:
    return False
  elif n == 2:
    return True

  for i in range(3, int(n**0.5 + 1), 2):
    if n % i == 0:
      return False

  return True

if __name__ == "__main__":

  count = 1
  num = 1

  while count < 10001:
    num += 2
    if is_prime(num):
      count += 1

  print(num)