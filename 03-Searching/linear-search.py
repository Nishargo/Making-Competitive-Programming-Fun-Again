def linear_search(arr, target):
    """
    Perform a linear search on the list 'arr' to find the 'target' element.
    
    :param arr: List of elements to search
    :param target: Element to find in the list
    :return: Index of the target element if found, otherwise -1
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

if __name__ == "__main__":
    # Prompt user to input the list elements
    user_input = input("Enter the list of numbers separated by spaces: ")
    
    # Convert the input string to a list of integers
    my_list = list(map(int, user_input.split()))
    
    # Prompt user to input the target element
    target_element = int(input("Enter the target element to search for: "))
    
    # Perform linear search
    result = linear_search(my_list, target_element)
    
    # Print the result
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list")
