def find_max_min_elements(arr):
    if len(arr) == 0:
        return None, None
    
    max_element = arr[0]
    min_element = arr[0]
    
    for num in arr:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num
    
    return max_element, min_element

# Example 
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_element, min_element = find_max_min_elements(array)
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")

# Can you write a user defined function?
