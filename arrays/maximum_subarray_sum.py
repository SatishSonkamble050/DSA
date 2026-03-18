"""
Problem: Maximum Subarray

Given an integer array nums, find the contiguous subarray
which has the largest sum and return its sum.

Example
-------
Input  : [2, 3, -8, 7, -1, 2, 3]
Output : 11

Explanation
-----------
The subarray [7, -1, 2, 3] has the maximum sum = 11
"""


# -----------------------------------------------------
# 1️⃣ BRUTE FORCE APPROACH
# -----------------------------------------------------
# Idea:
# Generate every possible subarray and calculate its sum.
#
# Time Complexity  : O(n³)
# Space Complexity : O(1)

def brute_force_max_subarray(arr):

    n = len(arr)
    max_sum = arr[0]

    for i in range(n):
        for j in range(i, n):

            current_sum = 0

            for k in range(i, j + 1):
                current_sum += arr[k]

            max_sum = max(max_sum, current_sum)

    return max_sum


# -----------------------------------------------------
# 2️⃣ BETTER APPROACH
# -----------------------------------------------------
# Idea:
# Instead of recalculating the sum again and again,
# extend the subarray sum progressively.
#
# Time Complexity  : O(n²)
# Space Complexity : O(1)

def better_max_subarray(arr):

    n = len(arr)
    max_sum = arr[0]

    for i in range(n):

        current_sum = 0

        for j in range(i, n):

            current_sum += arr[j]

            max_sum = max(max_sum, current_sum)

    return max_sum


# -----------------------------------------------------
# 3️⃣ OPTIMAL APPROACH (Kadane's Algorithm)
# -----------------------------------------------------
# Idea:
# At each position decide whether to:
# 1. Start a new subarray
# 2. Extend the previous subarray
#
# Formula:
# current_sum = max(arr[i], current_sum + arr[i])
#
# Time Complexity  : O(n)
# Space Complexity : O(1)

def optimal_max_subarray(arr):

    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = max(arr[i], current_sum + arr[i])

        max_sum = max(max_sum, current_sum)

    return max_sum


# -----------------------------------------------------
# DRIVER CODE
# -----------------------------------------------------

arr = [2, 3, -8, 7, -1, 2, 3]

print("Array:", arr)

print("\nBrute Force Result :", brute_force_max_subarray(arr))

print("\nBetter Approach Result :", better_max_subarray(arr))

print("\nOptimal Approach Result :", optimal_max_subarray(arr))