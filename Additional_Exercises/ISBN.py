isbn = [9,7,8,0,3,0,6,4,0,6,1,5]

last_digit_total = 0


for i in range(0, (len(isbn))):
    if i % 2 != 0:
        last_digit_total += (isbn[i] * 3)
    else:
        last_digit_total += isbn[i]

print(10 - (last_digit_total % 10))