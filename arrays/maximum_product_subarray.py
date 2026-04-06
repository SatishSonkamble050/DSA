# max_product_subarray.py

"""
Maximum Product Subarray

Given an integer array, find the contiguous subarray
that has the largest product.

This file includes:
1. Brute force approach (O(n^2))
2. Optimized approach (O(n))
"""


def max_product_brute(arr):
    """
    Brute Force Approach

    - Try all possible subarrays
    - Calculate product for each
    - Track maximum product

    Time Complexity: O(n^2)
    """
    max_value = float("-inf")
    n = len(arr)

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            max_value = max(max_value, product)

    return max_value


def max_product_optimized(arr):
    """
    Optimized Approach (Prefix + Suffix)

    Key Idea:
    - Product sign changes due to negative numbers
    - So we traverse from both directions:
        1. Left to Right (prefix)
        2. Right to Left (suffix)

    - Reset when product becomes 0

    Time Complexity: O(n)
    """
    max_value = float("-inf")
    prefix = 1
    suffix = 1

    n = len(arr)

    for i in range(n):

        # Reset if product becomes 0
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        # Left to Right product
        prefix *= arr[i]

        # Right to Left product
        suffix *= arr[n - i - 1]

        # Update maximum value
        max_value = max(max_value, prefix, suffix)

    return max_value


def main():
    """Example execution"""
    arr = [-2, 0, -1, 2]

    print("Input:", arr)
    print("Brute Force Result:", max_product_brute(arr))
    print("Optimized Result:", max_product_optimized(arr))


if __name__ == "__main__":
    main()