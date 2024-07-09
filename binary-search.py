# Binary search is an efficient algorithm used to find the position of a target value within a sorted array. 
# It works by repeatedly dividing the search interval in half. This method is known as "divide-and-concquer."
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Target not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")


