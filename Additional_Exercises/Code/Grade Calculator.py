maths = int(input("Please enter your Maths mark: "))
chem = int(input("Please enter your Chemistry mark: "))
phy = int(input("Please enter your Physics mark: "))

grade = maths + chem + phy
grade = grade / 3
print("Your percentage score is", grade)

if grade >= 70:
    print("You got an A")
elif grade >=60:
    print("You got a B")
elif grade >=50:
    print("You got a C")
elif grade >=40:
    print("You got a D")
else:
    print("You failed")