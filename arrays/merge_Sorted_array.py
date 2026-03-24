"""
Problem: Merge Two Sorted Arrays (LeetCode 88)

You are given:
nums1 = first sorted array with extra space at the end
nums2 = second sorted array

m = number of valid elements in nums1
n = number of elements in nums2

Task:
Merge nums2 into nums1 in-place such that nums1 becomes a sorted array.

Example:
nums1 = [1,7,8,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output:
[1,2,5,6,7,8]
"""

# --------------------------------------------------
# 🐢 1. BRUTE FORCE (Using Extra Array)
# --------------------------------------------------

def merge_brute(nums1, m, nums2, n):
    """
    Approach:
    - Use two pointers
    - Store result in a new array
    - Copy result back if needed

    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """

    p1 = 0
    p2 = 0
    result = []

    # Compare elements and add smaller one
    while p1 < m and p2 < n:
        if nums1[p1] < nums2[p2]:
            result.append(nums1[p1])
            p1 += 1
        else:
            result.append(nums2[p2])
            p2 += 1

    # Add remaining elements
    while p1 < m:
        result.append(nums1[p1])
        p1 += 1

    while p2 < n:
        result.append(nums2[p2])
        p2 += 1

    return result


# --------------------------------------------------
# ⚡ 2. OPTIMAL (In-Place, 3 Pointer Approach)
# --------------------------------------------------

def merge_optimal(nums1, m, nums2, n):
    """
    Approach:
    - Start from the END of both arrays
    - Place the largest element at the end of nums1

    Why from end?
    → To avoid overwriting existing values in nums1

    Pointers:
    p1 → last valid element in nums1
    p2 → last element in nums2
    p  → last index of nums1

    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """

    p1 = m - 1  # last valid index of nums1
    p2 = n - 1  # last index of nums2
    p = m + n - 1  # last index of nums1

    # Merge from the back
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If nums2 still has elements, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1


# --------------------------------------------------
# 🧪 TESTING
# --------------------------------------------------

if __name__ == "__main__":

    nums1 = [1,7,8,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    print("Brute Force Result:")
    print(merge_brute(nums1[:m], m, nums2, n))  
    # nums1[:m] → only valid elements

    print("\nOptimal In-Place Result:")
    print(merge_optimal(nums1, m, nums2, n))