"""
Bubble sort works by repeatedly stepping through the list, comparing adjacent items and swapping them if they are in the wrong order.
Each pass through the list places the next largest element in its correct position, bubbling it to the end of the list.

On the first pass, the largest element is moved to its correct position at the end of the list.
On the second pass, the second-largest element is moved to its correct position, and so on.

After each pass, the last i elements are already sorted.
Hence, in the i-th pass, there is no need to compare the last i elements again.
The inner loop runs from the start of the list to n - i - 1, effectively ignoring the last i elements which are already sorted.
"""

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
if __name__ == "__main__":
    # Sample array
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)

# Can you try it with a user defined function?
