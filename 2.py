"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

if __name__ == "__main__":
  fibs = dict()
  fibs[1], fibs[2] = 1, 2
  n, i, total = 100, 3, 2

  while True:
    fibs[i] = fibs[i-1] + fibs[i-2]
    if fibs[i] > 4000000: break
    if fibs[i] % 2 == 0: total += fibs[i]
    i += 1

  print(total)