"""
Write a script called exponent.py that receives two numbers from the
user and displays the first number raised to the power of the second
number.
A sample run of the program should look like this (with example input
that has been provided by the user included below):
Enter a base: 1.2
Enter an exponent: 3
1.2 to the power of 3 = 1.7279999999999998

"""


base = float(input("Enter a base: "))
exponent = float(input("Enter an exponent: "))
print(f"{base} to the power {exponent} = {base ** exponent}")
