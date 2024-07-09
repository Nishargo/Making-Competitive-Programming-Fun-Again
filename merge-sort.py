def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Sorting the first half
        merge_sort(left_half)
        
        # Sorting the second half
        merge_sort(right_half)
        
        i = j = k = 0
        
        # Copy data to temp arrays left_half[i] and right_half[j]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Helper function to print the array
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Test the merge_sort function
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is:")
    print_list(arr)
    
    merge_sort(arr)

  
    
    print("Sorted array is:")
    print_list(arr)

 # Can you try it with a user defined function? 

