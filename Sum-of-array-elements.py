#  The function 'sum_of_array_elements' takes a list of numbers as an argument and returns the sum of its elements.
def sum_of_array_elements(array):

    # Parameter:
    # array (list): A list of numerical elements.

    # The 'sum' function is used to compute the sum of the list. 
    
    total_sum = sum(array)
    return total_sum

# Example
array = [1, 2, 3, 4, 5]
print(f"The sum of the array elements is: {sum_of_array_elements(array)}")
