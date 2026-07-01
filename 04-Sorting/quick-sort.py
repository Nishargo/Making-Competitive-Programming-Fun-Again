def quick_sort(arr):
    """
    The main function that implements Quick Sort.
    arr : list of elements to be sorted
    """
    # Base case: If the array is empty or has one element, return it
    if len(arr) <= 1:
        return arr
    
    # Recursive case: Choose a pivot and divide the array
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
        left = [x for x in arr if x < pivot]  # Elements less than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        
        # Recursively apply quick_sort to the left and right divisions
        return quick_sort(left) + middle + quick_sort(right)

def get_user_input():
    """
    Function to get user input for the array to be sorted.
    Returns:
        list: The list of integers input by the user.
    """
    user_input = input("Enter numbers separated by spaces: ")
    user_list = [int(x) for x in user_input.split()]
    return user_list

if __name__ == "__main__":
    user_array = get_user_input()
    print("Original array:", user_array)
    sorted_array = quick_sort(user_array)
    print("Sorted array:", sorted_array)
