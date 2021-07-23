"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def euler_9():
  for a in range(1, 1000):
    for b in range(a + 1, 1000):
      c = (a**2 + b**2)**0.5

      if a + b + c > 1000:
        break
      elif c != int(c):
        continue
      elif a + b + c == 1000:
        return int(a*b*c)


if __name__ == "__main__":
  print(euler_9())