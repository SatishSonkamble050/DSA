"""
File: duplicate_number.py

Problem:
Find the duplicate number in an array.

Example:
Input:  [1, 3, 4, 2, 3, 3]
Output: 3

--------------------------------------------------
APPROACHES INCLUDED:
1. Brute Force
2. Sorting (Better)
3. HashMap (Optimal Practical)
4. Floyd’s Cycle Detection (Best Optimal)

--------------------------------------------------
HOW TO RUN:

1. Save file:
   duplicate_number.py

2. Run:
   python duplicate_number.py
"""

# --------------------------------------------------
# 1. BRUTE FORCE (O(n^2))
# --------------------------------------------------
def brute(arr):
    """
    Compare each element with previously seen elements
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    new_arr = []

    for i in arr:
        for j in new_arr:
            if i == j:
                return i
        new_arr.append(i)


# --------------------------------------------------
# 2. BRUTE IMPROVED (Using Set)
# --------------------------------------------------
def brute_improved(arr):
    """
    Use set to track seen elements
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()

    for i in arr:
        if i in seen:
            return i
        seen.add(i)


# --------------------------------------------------
# 3. SORTING APPROACH (O(n log n))
# --------------------------------------------------
def best(arr):
    """
    Sort array and check adjacent elements
    Time Complexity: O(n log n)
    Space Complexity: O(1) (if in-place)
    """
    arr = sorted(arr)  # safe (does not modify original)

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return arr[i]


# --------------------------------------------------
# 4. HASHMAP APPROACH (O(n))
# --------------------------------------------------
def optimize(arr):
    """
    Use dictionary for frequency count
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    hashmap = {}

    for i in arr:
        if i in hashmap:
            return i   # early return (optimized)
        hashmap[i] = 1




# --------------------------------------------------
# MAIN FUNCTION (TESTING)
# --------------------------------------------------
if __name__ == "__main__":
    nums = [1, 3, 4, 2, 3, 3]

    print("Input:", nums)

    print("\n--- Results ---")
    print("Brute:", brute(nums))
    print("Brute Improved (Set):", brute_improved(nums))
    print("Sorting (Best):", best(nums))
    print("HashMap (Optimize):", optimize(nums))