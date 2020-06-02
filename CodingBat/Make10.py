#Given 2 ints, a and b, return true if one if them is 10 or if their sum is 10.


#makes10(9, 10) → true
#makes10(9, 9) → false
#makes10(1, 9) → true


def makes10(a, b):
  if ((a + b == 10) or (a == 10) or (b == 10)):
    return True
  else:
    return False
