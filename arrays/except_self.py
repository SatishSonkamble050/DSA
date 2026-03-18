"""
Problem: Product of Array Except Self

Given an integer array nums, return an array answer such that:

answer[i] = product of all elements of nums except nums[i]

Constraints:
1. Do NOT use division in the optimal solution.
2. Time Complexity should be O(n).

Example:
Input  : [1,2,3,4]
Output : [24,12,8,6]

Explanation:
index 0 -> 2*3*4 = 24
index 1 -> 1*3*4 = 12
index 2 -> 1*2*4 = 8
index 3 -> 1*2*3 = 6
"""

# -----------------------------------------------------
# 1️⃣ BRUTE FORCE APPROACH
# -----------------------------------------------------
# Idea:
# For every index, multiply all elements except itself.
#
# Time Complexity  : O(n²)
# Space Complexity : O(n)

def brute_force_product(arr):

    result = []

    for i in range(len(arr)):

        product = 1

        for j in range(len(arr)):
            if i != j:
                product *= arr[j]

        result.append(product)

    return result


# -----------------------------------------------------
# 2️⃣ BETTER APPROACH (Prefix + Suffix Arrays)
# -----------------------------------------------------
# Idea:
# Instead of recalculating products every time,
# store prefix products and suffix products.
#
# prefix[i] = product of elements before i
# suffix[i] = product of elements after i
#
# result[i] = prefix[i] * suffix[i]
#
# Time Complexity  : O(n)
# Space Complexity : O(n)

def better_product(arr):

    n = len(arr)

    prefix = [1] * n
    suffix = [1] * n
    result = [0] * n

    # build prefix array
    for i in range(1, n):
        prefix[i] = arr[i-1] * prefix[i-1]

    # build suffix array
    for i in range(n-2, -1, -1):
        suffix[i] = arr[i+1] * suffix[i+1]

    # calculate result
    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result


# -----------------------------------------------------
# 3️⃣ OPTIMAL APPROACH (Using Division + Zero Handling)
# -----------------------------------------------------
# Idea:
# Multiply all non-zero elements.
#
# Case 1 → No zero
# answer[i] = total_product / arr[i]
#
# Case 2 → One zero
# Only index with zero gets product of others.
#
# Case 3 → More than one zero
# All results are zero.
#
# Time Complexity  : O(n)
# Space Complexity : O(n)

def optimal_product(arr):

    total_product = 1
    zero_count = 0
    zero_index = -1
    n = len(arr)

    # calculate total product and zero count
    for i in range(n):

        if arr[i] == 0:
            zero_count += 1
            zero_index = i
        else:
            total_product *= arr[i]

    result = [0] * n

    # Case 1: No zero
    if zero_count == 0:

        for i in range(n):
            result[i] = total_product // arr[i]

    # Case 2: One zero
    elif zero_count == 1:

        result[zero_index] = total_product

    # Case 3: More than one zero
    # result already contains all zeros

    return result


# -----------------------------------------------------
# DRIVER CODE
# -----------------------------------------------------

arr = [10, 0, 5, 0, 2]

print("Array:", arr)

print("\nBrute Force Output :", brute_force_product(arr))

print("\nBetter Approach Output :", better_product(arr))

print("\nOptimal Approach Output :", optimal_product(arr))