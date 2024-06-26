# import math library
import math

# function to get the absolute value of a number is abs ()

integer = -60
print('Absolute value of the given integer is', abs(integer))

# function to return the value (in float) of the first parameter and the sign of the second parameter
print(math.copysign(3,-98.4) #This should return -3.0

# function to return the factorial of number, it only accepts positive integers.
print(math.factorial(5)) #This should return 120
      
# function to round a number upward (imagine a ceiling) to its nearest integer
print(math.ceil(1.8)) #This should return 2
      
# function to round a number down (imagine a floor) to its nearest integer
print(math.floor(1.2)) #This should return 1

#function to find the greatest common divisor of the two integers
print (math.gcd(3, 6)) #This should return 3

#function to return the remainder of x/y
print(math.fmod(20, 4)) #This should return 0

#function to return the square root of a number
print(math.sqrt(2)) #This should return 1.4142135623730951

# max() function to get maximum value from a sequence of a list, tuple, or set
x = [4, 5, 6, 7, 8]
y = max(x)
print(y) #This should return 8


