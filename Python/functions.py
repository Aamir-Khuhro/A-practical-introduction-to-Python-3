def multiply(x,y):
    result = x * y
    return result

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(f"The product of {num1} and {num2} is {multiply(num1,num2): .2f}.")

for i in range(1,6):
    for j in range(i):
        print("*", end=' ')
    print("")
