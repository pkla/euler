"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from time import time

def largest_palindrome_product(naive=False, n=3):
  if naive:
    ### Naive
    best = 0
    for i in range(1000000, 10000000):
      for j in range(1000000, 10000000):
        prod = i*j
        prod_str = str(prod)
        if prod_str == prod_str[::-1]:
          best = max(best, prod)
    return best

  nums = list(range(10**n-1, 10**(n-1) - 1, -1))

  for i in range(len(nums)):
    ceil = i // 2 + 1
    for j in range(ceil):
      col = ceil - j - 1
      row = i - col
      prod = str(nums[col]*nums[row])
      if prod == prod[::-1]:
        return int(prod)

if __name__ == "__main__":
  for n in range(2, 15):
    start = time()
    print(largest_palindrome_product(naive=False, n=n))
    print(f"digits={n} ==> {time()-start:.2f}s")