"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

DIGIT_TO_WORD = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

TEEN_TO_WORD = {
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen"
}

TEN_TO_WORD = {
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}

def spell_integer(n: int) -> str:
    if 0 < n < 10:
        return DIGIT_TO_WORD[n]
    elif n < 20:
        return TEEN_TO_WORD[n]
    elif n < 100:
        return TEN_TO_WORD[n//10*10] + DIGIT_TO_WORD[int(str(n)[1])]
    elif not n % 100 and n < 1000:
        return DIGIT_TO_WORD[int(str(n)[0])] + "hundred"
    elif n < 110:
        n_as_str = str(n)
        return "onehundredand" + spell_integer(int(n_as_str[1:3]))
    elif n < 1000:
        n_as_str = str(n)
        return DIGIT_TO_WORD[int(n_as_str[0])] + "hundredand" + spell_integer(int(n_as_str[1:3]))
    elif n == 1000:
        return "onethousand"

def letters_in_integer(n: int) -> int:
    if 0 < n < 10:
        return len(DIGIT_TO_WORD[n])
    elif n < 20:
        return len(TEEN_TO_WORD[n])
    elif n < 100:
        return len(TEN_TO_WORD[n//10*10]) + len(DIGIT_TO_WORD[int(str(n)[1])])
    elif not n % 100 and n < 1000:
        return len(DIGIT_TO_WORD[int(str(n)[0])]) + 7
    elif n < 110:
        n_as_str = str(n)
        return 13 + letters_in_integer(int(n_as_str[1:3]))
    elif n < 1000:
        n_as_str = str(n)
        return len(DIGIT_TO_WORD[int(n_as_str[0])]) + 10 + letters_in_integer(int(n_as_str[1:3]))
    elif n == 1000:
        return 11

def euler_17():
    total = 0
    for n in range(1, 1001):
        total += letters_in_integer(n)
    return total

if __name__ == "__main__":
    print(euler_17())