"""
What is the value of the first triangle number to have over five hundred divisors?
"""

def count_divisors(n, start):
  if n == 1:
    return 1

  for i in range(start, int(n**0.5)+1):
    if n % i == 0:
      count = 1
      while (n % i == 0):
        n /= i
        count += 1

      return count*count_divisors(n, i+1)

  return 2

def euler_12():
  ceil = 0
  n = 0
  count = 0

  while count < 500:
    ceil += 1
    n = n + ceil

    count = count_divisors(n, 2)

  return n

if __name__ == "__main__":
  print(euler_12())