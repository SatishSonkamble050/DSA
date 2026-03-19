"""
3SUM PROBLEM - COMPLETE GUIDE
=============================

This file contains:
1. Brute Force Solution (O(n^3))
2. Better (Set-based) Solution (O(n^2))
3. Optimal Two Pointer Solution (O(n^2))
4. Micro-Optimized Solution (Best Practical)

Problem:
--------
Given an array nums, return all unique triplets [a, b, c] such that:
    a + b + c = 0

------------------------------------------------------------
"""


# ------------------------------------------------------------
# 1. BRUTE FORCE SOLUTION
# ------------------------------------------------------------
# Idea:
# Try all possible triplets using 3 loops
# Time Complexity: O(n^3)
# Space Complexity: O(n^2) (for storing results)


def three_sum_brute(arr):
    n = len(arr)
    result = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()  # normalize order

                    # avoid duplicates
                    if temp not in result:
                        result.append(temp)

    return result


# ------------------------------------------------------------
# 2. BETTER SOLUTION (USING SET - 2SUM IDEA)
# ------------------------------------------------------------
# Idea:
# Fix one element and use a set to find remaining two
# Time Complexity: O(n^2)
# Space Complexity: O(n)


def three_sum_better(arr):
    n = len(arr)
    result = set()

    for i in range(n):
        seen = set()
        for j in range(i + 1, n):
            target = -(arr[i] + arr[j])

            if target in seen:
                temp = tuple(sorted([arr[i], arr[j], target]))
                result.add(temp)

            seen.add(arr[j])

    return list(result)


# ------------------------------------------------------------
# 3. OPTIMAL SOLUTION (TWO POINTER)
# ------------------------------------------------------------
# Idea:
# 1. Sort array
# 2. Fix one element
# 3. Use two pointers for remaining
#
# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding output)


def three_sum_optimal(arr):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n):

        # skip duplicate values for i
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])

                left += 1
                right -= 1

                # skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ------------------------------------------------------------
# 4. MICRO-OPTIMIZED SOLUTION (BEST PRACTICAL)
# ------------------------------------------------------------
# Additional Improvements:
# - Early break if arr[i] > 0
# - Skip impossible cases
#
# Time Complexity: O(n^2)
# But faster in real scenarios


def three_sum_optimized(arr):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n):

        # skip duplicates
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # early stopping
        if arr[i] > 0:
            break

        # smallest sum > 0
        if i + 2 < n and arr[i] + arr[i + 1] + arr[i + 2] > 0:
            break

        # largest sum < 0
        if arr[i] + arr[n - 1] + arr[n - 2] < 0:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])

                left += 1
                right -= 1

                # skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ------------------------------------------------------------
# TESTING ALL METHODS
# ------------------------------------------------------------

if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]

    print("Input:", arr)
    print("\nBrute Force:", three_sum_brute(arr))
    print("Better (Set):", three_sum_better(arr))
    print("Optimal (Two Pointer):", three_sum_optimal(arr))
    print("Micro Optimized:", three_sum_optimized(arr))


"""
------------------------------------------------------------
SUMMARY
------------------------------------------------------------

| Approach          | Time Complexity | Space |
|------------------|---------------|-------|
| Brute Force      | O(n^3)        | O(n^2)|
| Better (Set)     | O(n^2)        | O(n)  |
| Optimal          | O(n^2)        | O(1)  |
| Micro Optimized  | O(n^2)        | O(1)  |

------------------------------------------------------------
INTERVIEW TIP:
------------------------------------------------------------
Always explain evolution:
1. Start with brute force
2. Reduce to 2Sum
3. Apply sorting + two pointers
4. Handle duplicates carefully

That's what interviewers expect 🚀
------------------------------------------------------------
"""
