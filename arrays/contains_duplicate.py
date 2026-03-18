"""
Contains Duplicate Problem

Given an integer array nums, return True if any value appears at least twice,
otherwise return False.

This file includes all approaches:
1. Brute Force
2. Sorting
3. HashSet (Optimal)
4. One-liner (Pythonic)
"""


# 🔹 1. Brute Force Approach
# Time: O(n^2), Space: O(1)
def contains_duplicate_bruteforce(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


# 🔹 2. Sorting Approach
# Time: O(n log n), Space: O(1) (in-place)
def contains_duplicate_sorting(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False


# 🔹 3. HashSet Approach (Optimal)
# Time: O(n), Space: O(n)
def contains_duplicate_hashset(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False


# 🔹 4. One-Liner Approach
# Time: O(n), Space: O(n)
def contains_duplicate_oneliner(arr):
    return len(arr) != len(set(arr))


# 🔹 Test Cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 1],     # True
        [1, 2, 3, 4],     # False
        [1, 1, 1, 3, 3],  # True
        [],               # False
        [10]              # False
    ]

    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {arr}")
        print("Brute Force   :", contains_duplicate_bruteforce(arr.copy()))
        print("Sorting       :", contains_duplicate_sorting(arr.copy()))
        print("HashSet       :", contains_duplicate_hashset(arr.copy()))
        print("One-Liner     :", contains_duplicate_oneliner(arr.copy()))