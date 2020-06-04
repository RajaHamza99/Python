import pytest


def string_match(a, b):
  length = min(len(a), len(b))
  count = 0
  
  for i in range (length-1):
    a_string = a[i:i+2]
    b_string = b[i:i+2]
    
    if a_string == b_string:
      count += 1
      
  return count