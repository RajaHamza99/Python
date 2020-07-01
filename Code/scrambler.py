"""CHALLENGE OF THE DAY
 
Write a python function that takes a 4 digit number and a word with 5 letters and scrambles them up.
 
Example: scarmble(12345,abcde) ----> 1a2b3c4d5e"""

import random

def scramble(numbers, letters):
    num_list = []
    char_list = []
    for i in numbers:
        num_list.append(i)
    for x in letters:
        char_list.append(i)
    random.shuffle(num_list)
    random.shuffle(char_list)
