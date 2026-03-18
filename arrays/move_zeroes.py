"""
Move Zeroes Problem

Given an integer array, move all 0's to the end while maintaining
the relative order of non-zero elements.

------------------------------------------------------------
Approaches Included:
1. Brute Force (Sorting based idea)
2. Two Pointer + Shifting (Inefficient)
3. Extra Array (Better)
4. Optimal In-place (Best)
------------------------------------------------------------
"""


# 🔹 1. Brute Force (Sorting idea - NOT recommended)
# -------------------------------------------------
# Idea:
# Sort array in descending order so that zeros go to end
# ❌ Problem: Order of elements is NOT preserved
# ❌ Not valid for actual problem requirement
# Time: O(n log n)
# Space: O(1)

def brute_force(arr):
    arr.sort(reverse=True)
    return arr


# 🔹 2. Two Pointer + Shifting (Your approach)
# -------------------------------------------------
# Idea:
# When 0 is found, shift all elements left and place 0 at end
# ❌ Inefficient due to repeated shifting
# Time: O(n^2)
# Space: O(1)

def shift_left(arr, p, right):
    while p < right:
        arr[p] = arr[p + 1]
        p += 1


def two_pointer_shift(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        if arr[left] == 0:
            if arr[right] == 0:
                right -= 1
                continue

            temp = arr[left]
            shift_left(arr, left, right)
            arr[right] = temp
            right -= 1
        else:
            left += 1

    return arr


# 🔹 3. Extra Array Approach (Better)
# -------------------------------------------------
# Idea:
# Copy all non-zero elements first, then fill remaining with zeros
# Time: O(n)
# Space: O(n)

def extra_array(arr):
    new_arr = [0] * len(arr)
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr[j] = arr[i]
            j += 1

    return new_arr


# 🔹 4. Optimal Approach (Best - In-place Two Pointer)
# -------------------------------------------------
# Idea:
# Maintain pointer j for next non-zero position
# Swap when non-zero is found
# Time: O(n)
# Space: O(1)

def optimal(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]   # swap
            j += 1

    return arr


# 🔹 Test Cases
# -------------------------------------------------
if __name__ == "__main__":
    arr = [1, 4, 6, 0, 7, 2, 0, 3, 5]

    print("Original Array        :", arr)

    print("\nBrute Force           :", brute_force(arr.copy()))
    print("Two Pointer Shift     :", two_pointer_shift(arr.copy()))
    print("Extra Array           :", extra_array(arr.copy()))
    print("Optimal (Best)        :", optimal(arr.copy()))