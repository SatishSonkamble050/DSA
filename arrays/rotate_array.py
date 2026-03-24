"""
📘 Array Rotation (Right Rotation by K)

This file contains:
1. Brute Force Approach
2. Better Approach (Using Extra Space)
3. Optimal Approach (Reversal Algorithm)

Author: Sateesh Sonkamble
"""

# ---------------------------------------------------
# 🔴 1. Brute Force Approach
# Time: O(n * k), Space: O(1)
# ---------------------------------------------------

def brute_force(arr, k):
    n = len(arr)

    for _ in range(k):
        temp = arr[n - 1]

        for j in range(n - 1, -1, -1):
            if j != 0:
                arr[j] = arr[j - 1]
            else:
                arr[j] = temp

    return arr


# ---------------------------------------------------
# 🟡 2. Better Approach (Using Extra Array)
# Time: O(n), Space: O(k)
# ---------------------------------------------------

def better(arr, k):
    n = len(arr)
    k = k % n

    # Step 1: store last k elements
    temp = arr[n - k:]

    # Step 2: shift remaining elements
    for i in range(n - 1, k - 1, -1):
        arr[i] = arr[i - k]

    # Step 3: place temp elements at front
    for i in range(k):
        arr[i] = temp[i]

    return arr


# ---------------------------------------------------
# 🟢 3. Optimal Approach (Reversal Algorithm)
# Time: O(n), Space: O(1)
# ---------------------------------------------------

def optimize(arr, k):
    n = len(arr)
    k = k % n

    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    # Step 1: reverse whole array
    reverse(0, n - 1)

    # Step 2: reverse first k elements
    reverse(0, k - 1)

    # Step 3: reverse remaining elements
    reverse(k, n - 1)

    return arr


# ---------------------------------------------------
# 🚀 Main Execution
# ---------------------------------------------------

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    arr3 = [1, 2, 3, 4, 5, 6, 7]

    k = 3

    print("Brute Force  :", brute_force(arr1.copy(), k))
    print("Better       :", better(arr2.copy(), k))
    print("Optimized    :", optimize(arr3.copy(), k))