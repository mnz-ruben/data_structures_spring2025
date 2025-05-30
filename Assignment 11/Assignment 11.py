#!/usr/bin/env python3
"""
sort_algorithms.py

Implements Insertion Sort and Bubble Sort algorithms.
"""

def insertion_sort(arr):
    """
    Sorts a list in place using the insertion sort algorithm.
    Returns the sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    """
    Sorts a list in place using the bubble sort algorithm.
    Returns the sorted list.
    """
    n = len(arr)
    for i in range(n):
        # After i passes, the last i elements are in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent out-of-order elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:      ", data)

    ins_sorted = insertion_sort(data.copy())
    print("After Insertion Sort:", ins_sorted)

    bub_sorted = bubble_sort(data.copy())
    print("After Bubble Sort:   ", bub_sorted)

if __name__ == "__main__":
    main()
