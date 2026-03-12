"""
Problem: Count Number of Pairs with Given Sum

Given a sorted array and a target value,
count how many pairs (i, j) exist such that:

arr[i] + arr[j] = target
i < j

Example
-------
arr = [-1, 1, 5, 5, 5, 7]
target = 6

Pairs:
(1,5)
(1,5)
(1,5)

Output: 3
"""

# ------------------------------------------------
# 1️⃣ BRUTE FORCE APPROACH
# ------------------------------------------------
# Check every possible pair
# Time Complexity : O(n²)
# Space Complexity: O(1)

def brute_force_two_sum(arr, target):

    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            if arr[i] + arr[j] == target:
                count += 1

    return count


# ------------------------------------------------
# 2️⃣ BETTER APPROACH (Hash Map)
# ------------------------------------------------
# Store seen numbers in dictionary
# If target - current exists → valid pair
#
# Time Complexity : O(n)
# Space Complexity: O(n)

def better_two_sum(arr, target):

    seen = {}
    count = 0

    for num in arr:

        complement = target - num

        if complement in seen:
            count += seen[complement]

        seen[num] = seen.get(num, 0) + 1

    return count


# ------------------------------------------------
# 3️⃣ OPTIMAL APPROACH (Two Pointer)
# ------------------------------------------------
# Works when array is sorted
#
# Time Complexity : O(n)
# Space Complexity: O(1)

def optimal_two_sum(arr, target):

    left = 0
    right = len(arr) - 1
    count = 0

    while left < right:

        current = arr[left] + arr[right]

        # pair found
        if current == target:

            # case when values are same
            if arr[left] == arr[right]:
                n = right - left + 1
                count += (n * (n - 1)) // 2
                break

            left_value = arr[left]
            right_value = arr[right]

            left_count = 0
            right_count = 0

            # count duplicates from left
            while left <= right and arr[left] == left_value:
                left_count += 1
                left += 1

            # count duplicates from right
            while right >= left and arr[right] == right_value:
                right_count += 1
                right -= 1

            count += left_count * right_count

        elif current < target:
            left += 1
        else:
            right -= 1

    return count


# ------------------------------------------------
# DRIVER CODE
# ------------------------------------------------

arr = [-1, 1, 5, 5, 5, 7]
target = 6

print("Array :", arr)
print("Target:", target)

print("\nBrute Force Count :", brute_force_two_sum(arr, target))

print("\nBetter Approach Count :", better_two_sum(arr, target))

print("\nOptimal Approach Count :", optimal_two_sum(arr, target))