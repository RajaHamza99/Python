#Description
#ISBN's (International Standard Book Numbers) are identifiers for books. 

#The ISBN is a thirteen-digit code.

#The last digit is a check number calculated as follows:
#•	The first 12 digits are taken
#•	Starting at index 1, if the index is odd - add it, and if the index is even – multiply the digit by three then add it.
#•	From the sum find the remainder after dividing by 10.
#•	10 minus the remainder give us the check digit
#•	In other words the following algebra would give us the check digit:
#( 10 – (( x1 + 3x2 + x3 + 3x4 + x5 + 3x6 + x7 + 3x8 + x9 + 3x10 + x11 + 3x12 ) % 10))

#For ISBN: 978-0-306-40615-? The following check would happen:
#•	9 +  3*7 +   8 +   3*0 +   3 +   3*0 +   6 +  3*4 +   0 +  3*6 + 1 +  3*5 = 93
#•	93 / 10 =
#Example


isbn = [9,7,8,0,3,0,6,4,0,6,1,5]

last_digit_total = 0


for i in range(0, (len(isbn))):
    if i % 2 != 0:
        last_digit_total += (isbn[i] * 3)
    else:
        last_digit_total += isbn[i]

print(10 - (last_digit_total % 10))