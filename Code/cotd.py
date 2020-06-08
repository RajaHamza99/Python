"""CHALLENGE OF THE DAY
 

Write a FUNCTION which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

 

So if 2 was the input, the function should return 2+22+222+2222 which is 2468.  


three(9) → 11106
three(5) → 6170 

HINT
What happens if you multiply a string by a number?"""


def add(input):
    num = int(input)
    num1 = int(input * 11)
    num2 = int(input * 111)
    num3 = int(input * 1111)
    total = num + num1 + num2 + num3
    return total