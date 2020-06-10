"""Flask CHALLENGE OF THE DAY
Given two Strings of equal length, 'merge' them into one String.

 

    # Do this by 'zipping' the Strings together.

 

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

 

    # Maintain case.

 

    # You will not encounter whitespace.
    
    # <EXAMPLES>

 

    # four("String","Fridge") → "SFtrriidngge"
    # four("Dog","Cat") → "DCoagt"
    # four("True","Tree") → "TTrrueee" 
    # four("return","letter") → "rleettutrenr"

 

    # <HINT>
    # Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    # How would you seperate a string into characters?"""



def zip(first, second):
    word = []
    for i in range (len(first)):
        word.append(first[i])
        word.append(second[i])
    string = "".join(word)
    return string