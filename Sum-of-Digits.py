# Extracting Digits from an Integer
# When you have an integer, the digits are not directly accessible in the same way they are in a string. 
# To extract each digit from the integer, you need to use a combination of the modulo (%) and integer division (//) operators.

# The modulo operator is used to get the remainder of a division operation. 
# For example, 123 % 10 results in 3, which is the last digit of 123.

# Integer division is used to remove the last digit of the number. 
# For example, 123 // 10 results in 12, effectively removing the last digit (3).

# By repeatedly using the modulo operator to extract the last digit and then using integer division to remove the last digit, you can iterate over all the digits in the number.

def sum_of_digits(number):
    total = 0
    while number > 0:
      #Add the last digit to the total
        total += number % 10  
       #Remove the last digit
        number //= 10         
    return total


