"""Question: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to
 the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,9,25,49,81

 

func(2,4,6,8,9) ------> 81

func(1,3) ---------> 1,9"""

 

def square(list):
    squared = []
    for i in list:
        if i % 2 != 0:
            x = i * i
            squared.append(x)
    return squared
