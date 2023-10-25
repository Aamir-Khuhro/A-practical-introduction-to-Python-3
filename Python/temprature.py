"""

Write a script called temperature.py that defines two functions:
1. convert_cel_to_far() which takes one float parameter representing
   degrees Celsius and returns a float representing the same temperature
   in degrees Fahrenheit using the following formula:
   F = C * 9/5 + 32
2. convert_far_to_cel() which take one float parameter representing
   degrees Fahrenheit and returns a float representing the same temperature
   in degrees Celsius using the following formula:
   C = (F - 32) * 5/9
   
"""
 
def convert_cel_to_far(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def convert_far_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
    
fahrenheit = int(input("Enter a temperature in degrees F: "))
print(f"{fahrenheit} degrees F = {convert_far_to_cel(fahrenheit): .2f} degrees C")
print("")
celsius = int(input("Enter a temperature in degrees C: "))
print(f"{celsius} degrees C = {convert_cel_to_far(celsius): .2f} degrees F")
