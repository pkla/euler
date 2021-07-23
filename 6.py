"""
The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is  3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

if __name__ == "__main__":
  sum_square = sum([n**2 for n in range(1, 101)])
  square_sum = sum(range(1, 101))**2
  print(sum_square, square_sum)