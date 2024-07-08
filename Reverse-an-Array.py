# The function `reverse_array` takes an array as an input and returns a new array that is the reverse of the input.
def reverse_array(arr):
# The slicing syntax `arr[::-1]` is used to reverse the array.

    return arr[::-1]

# Example usage
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    print("Original array:", array)
    reversed_array = reverse_array(array)
    print("Reversed array:", reversed_array)

# Can you create a user defined function?
