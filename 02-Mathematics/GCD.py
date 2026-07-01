# Example Calculation:
# To find the GCD of 48 and 18:

# gcd(48, 18)
# a = 48, b = 18
# First iteration: a = 18, b = 48 % 18 = 12
# Second iteration: a = 12, b = 18 % 12 = 6
# Third iteration: a = 6, b = 12 % 6 = 0
# b is now 0, so the GCD is 6.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function with example inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
