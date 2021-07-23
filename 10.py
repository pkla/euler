"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def is_prime(n):
  if n < 2: return False
  elif n == 2: return True

  for i in range(3, int(n**0.5 + 1), 2):
    if n % i == 0: return False

  return True

if __name__ == "__main__":

  num = 3
  result = 2
  ceil = 2*10**6

  while num < ceil:
    if is_prime(num):
      result += num
    num += 2

  print(result)