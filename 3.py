"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
  if n % 2 == 0:
    return False

  for i in range(3, int(n**0.5) + 1, 2):
    if n % i == 0:
      return False

  return True

if __name__ == "__main__":
  n = 600851475143

  start = int(n**0.5)
  if start % 2 == 0:
    start = start + 1

  for i in range(start, 2, -2):
    if n % i == 0 and is_prime(i):
      print(i)
      break