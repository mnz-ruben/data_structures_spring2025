#!/usr/bin/env python3
"""
binary_search_demo.py

Implements binary search on a sorted array.
"""

from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Perform binary search on a sorted list `arr` to find `target`.
    Returns the index of `target` if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    # Example usage
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Sorted list:", sorted_list)

    targets = [7, 2, 19, 20]
    for t in targets:
        idx = binary_search(sorted_list, t)
        if idx != -1:
            print(f"Target {t} found at index {idx}.")
        else:
            print(f"Target {t} not found in the list.")

if __name__ == "__main__":
    main()
