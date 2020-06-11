"""
    Write a function which returns the boolean True if the input is only divisible by one and itself.
    
    The function should return the boolean False if not.
    two(3) → True
    two(8) → False"""

def div(input):
    if input > 1:
        for i in range (2, input):
            if input % i == 0:
                return False
    return True

print(div(3))