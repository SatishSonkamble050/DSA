"""
Majority Element Problem
------------------------
Find the element that appears more than n/2 times in an array.

Example:
Input: [3,2,3]
Output: 3
"""

# -----------------------------
# 1. BRUTE FORCE (Hash Map)
# -----------------------------
def brute(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Approach:
    - Count frequency using dictionary
    - Return element if count >= n/2
    """
    n = len(arr)
    majority_count = n // 2
    hashmap = {}

    for num in arr:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    for key in hashmap:
        if hashmap[key] > majority_count:
            return key

    return "No Majority Element"


# -----------------------------
# 2. BETTER APPROACH (Sorting)
# -----------------------------
def better(arr):
    """
    Time Complexity: O(n log n)
    Space Complexity: O(1)

    Approach:
    - Sort the array
    - Majority element will always be at index n//2
    """
    arr.sort()
    candidate = arr[len(arr) // 2]

    # Verify (important step)
    if arr.count(candidate) > len(arr) // 2:
        return candidate

    return "No Majority Element"


# -----------------------------
# 3. OPTIMAL (Boyer-Moore Voting)
# -----------------------------
def optimize(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    Approach:
    - Maintain count and candidate
    - Increase/decrease count
    - Final candidate may be majority → verify it
    """
    count = 0
    candidate = None

    # Step 1: Find candidate
    for num in arr:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate

    return "No Majority Element"


# -----------------------------
# MAIN FUNCTION
# -----------------------------
if __name__ == "__main__":
    arr = [3, 2, 3]

    print("Array:", arr)
    print("Brute Result   :", brute(arr))
    print("Better Result  :", better(arr))
    print("Optimal Result :", optimize(arr))