"""
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3  ("abc")
"""

# -------------------------------
# 1. BRUTE FORCE APPROACH
# -------------------------------
def brute_force(s):
    """
    Time Complexity: O(n^3)
    Space Complexity: O(1)

    Generate all substrings and check uniqueness
    """
    n = len(s)
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]

            # Check if all characters are unique
            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))

    return max_length


# -------------------------------
# 2. BETTER APPROACH
# -------------------------------
def better_approach(s):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Use set and break when duplicate found
    """
    n = len(s)
    max_length = 0

    for i in range(n):
        check_set = set()

        for j in range(i, n):
            if s[j] in check_set:
                break

            check_set.add(s[j])
            max_length = max(max_length, j - i + 1)

    return max_length


# -------------------------------
# 3. OPTIMAL APPROACH (SLIDING WINDOW)
# -------------------------------
def optimal_approach(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    Sliding window with two pointers
    """
    check_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in check_set:
            check_set.remove(s[left])
            left += 1

        check_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# -------------------------------
# DRIVER CODE
# -------------------------------
if __name__ == "__main__":
    s = "abcabcbb"

    print("Input:", s)
    print("Brute Force:", brute_force(s))
    print("Better Approach:", better_approach(s))
    print("Optimal Approach:", optimal_approach(s))