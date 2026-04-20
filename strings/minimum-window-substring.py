"""
Minimum Window Substring Problem

Problem:
Given two strings s and t, return the smallest substring of s
that contains all characters of t.

Example:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"

--------------------------------------------------
Approaches:
1. Brute Force
2. Better Approach
3. Optimized Sliding Window
--------------------------------------------------

Git Commands:

1. Add file:
   git add .

2. Commit changes:
   git commit -m "Add brute force, better, and optimized minimum window substring solutions"

3. Push code:
   git push origin main
"""

from collections import Counter


# --------------------------------------------------
# 1. Brute Force Solution
# --------------------------------------------------
# Explanation:
# - Start from every index
# - Build substring character by character
# - Check if substring contains all characters of t
# - Store the smallest valid substring
#
# Time Complexity: O(n^2 * m)
# Space Complexity: O(m)
# Time Complexity: O(n^2 * m)
# --------------------------------------------------
def brute_force_min_window(s, t):
    result = ""
    min_length = float("inf")

    for i in range(len(s)):
        target = {}

        # Store frequency of characters in t
        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        for j in range(i, len(s)):
            current_char = s[j]

            if current_char in target:
                target[current_char] -= 1

            # Check whether all required characters are matched
            if all(value <= 0 for value in target.values()):
                current_window = s[i:j + 1]

                if len(current_window) < min_length:
                    min_length = len(current_window)
                    result = current_window

                break

    return result


# --------------------------------------------------
# 2. Better Solution
# --------------------------------------------------
# Explanation:
# - Similar to brute force
# - Instead of checking all hashmap values every time,
#   use a count variable to track remaining characters
# - Faster than brute force
#
# Time Complexity: O(n^2)
# Space Complexity: O(m)
# Time Complexity: O(n^2)
# --------------------------------------------------
def better_min_window(s, t):
    result = ""
    min_length = float("inf")

    for i in range(len(s)):
        hashmap = {}

        # Store required character count
        for ch in t:
            hashmap[ch] = hashmap.get(ch, 0) + 1

        count = len(t)

        for j in range(i, len(s)):
            if s[j] in hashmap:
                if hashmap[s[j]] > 0:
                    count -= 1

                hashmap[s[j]] -= 1

            # If all required characters are found
            if count == 0:
                current_window = s[i:j + 1]

                if len(current_window) < min_length:
                    min_length = len(current_window)
                    result = current_window

                break

    return result


# --------------------------------------------------
# 3. Optimized Sliding Window Solution
# --------------------------------------------------
# Explanation:
# - Use two pointers: left and right
# - Expand right pointer to include characters
# - Shrink left pointer when all required characters are found
# - Always maintain the minimum valid window
#
# Time Complexity: O(n)
# Space Complexity: O(m)
# Time Complexity: O(n)
# --------------------------------------------------
def optimized_min_window(s, t):
    if not s or not t:
        return ""

    target_count = Counter(t)
    required = len(target_count)

    window_count = {}
    formed = 0

    left = 0
    min_len = float("inf")
    result = ""

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        # Check if current character satisfies required frequency
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Shrink the window while it is valid
        while left <= right and formed == required:
            current_window = s[left:right + 1]

            if len(current_window) < min_len:
                min_len = len(current_window)
                result = current_window

            left_char = s[left]
            window_count[left_char] -= 1

            if left_char in target_count and window_count[left_char] < target_count[left_char]:
                formed -= 1

            left += 1

    return result


# --------------------------------------------------
# Driver Code
# --------------------------------------------------
s = "ADOBECODEBANC"
t = "ABC"

print("Input String:", s)
print("Target String:", t)
print()

print("Brute Force Result:", brute_force_min_window(s, t))
print("Better Result:", better_min_window(s, t))
print("Optimized Result:", optimized_min_window(s, t))
