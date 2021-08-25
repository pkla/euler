"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sum_digits(n: int) -> int:
    result = 0
    for digit in str(n):
        result += int(digit)

    return result

def euler_16():
    return(sum_digits(2**1000))

if __name__ == "__main__":
    print(euler_16())