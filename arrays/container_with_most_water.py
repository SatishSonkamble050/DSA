"""
Container With Most Water

Problem:
Given an array of heights, find two lines that together with the x-axis
form a container such that the container contains the most water.

------------------------------------------------------------
Approaches Included:
1. Brute Force
2. Better (Still Brute Optimized Thinking)
3. Optimal (Two Pointer)
------------------------------------------------------------
"""


# 🔹 1. Brute Force Approach
# -------------------------------------------------
# Idea:
# Check all possible pairs and calculate area
# Time: O(n^2)
# Space: O(1)

def brute_force(arr):
    max_water = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            height = min(arr[i], arr[j])
            max_water = max(max_water, width * height)

    return max_water


# 🔹 2. Better Approach (Same as brute but cleaner thinking)
# -------------------------------------------------
# Idea:
# Same logic, but slightly optimized structure
# (Still O(n^2), just better readability)

def better(arr):
    max_water = 0

    for left in range(len(arr)):
        for right in range(left + 1, len(arr)):
            max_water = max(
                max_water,
                (right - left) * min(arr[left], arr[right])
            )

    return max_water


# 🔹 3. Optimal Approach (Two Pointer) ⭐
# -------------------------------------------------
# Idea:
# Start from both ends
# Move pointer with smaller height
# Time: O(n)
# Space: O(1)

def optimal(arr):
    left = 0
    right = len(arr) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(arr[left], arr[right])

        # calculate area
        max_water = max(max_water, width * height)

        # move smaller height pointer
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_water


# 🔹 Test Cases
# -------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        [1, 5, 4, 3],              # 6
        [3, 1, 2, 4, 5],           # 12
        [2, 1, 8, 6, 4, 6, 5, 5],  # 25
        [1, 1],                    # 1
    ]

    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {arr}")
        print("Brute Force :", brute_force(arr))
        print("Better      :", better(arr))
        print("Optimal ⭐   :", optimal(arr))