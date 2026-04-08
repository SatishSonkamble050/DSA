"""
Problem: Valid Palindrome

Check if a given string is a palindrome.
A palindrome reads the same forward and backward.

Constraints:
- Ignore non-alphanumeric characters
- Case-insensitive

Example:
Input: "A man, a plan, a canal Panama"
Output: True
"""


# -----------------------------------
# 🔹 1. Brute Force Approach (Clean + Reverse)
# -----------------------------------
def brute_force(s: str) -> bool:
    """
    Step 1: Remove non-alphanumeric characters
    Step 2: Convert to lowercase
    Step 3: Compare with reversed string

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    import re

    cleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    return cleaned == cleaned[::-1]


# -----------------------------------
# 🔹 2. Optimized Approach (Two Pointers)
# -----------------------------------
def optimized_approach(s: str) -> bool:
    """
    Use two pointers without creating extra space.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(s) - 1

    while left < right:

        # Skip non-alphanumeric (left side)
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric (right side)
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# -----------------------------------
# 🔹 Main Execution
# -----------------------------------
if __name__ == "__main__":
    s1 = "A man, a plan, a canal Panama"

    print("Input:", s1)

    print("\nBrute Force Result:", brute_force(s1))
    print("Optimized Approach Result:", optimized_approach(s1))