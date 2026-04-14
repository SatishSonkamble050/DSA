"""
📌 Longest Palindromic Substring - Complete Guide

We will solve the problem using 3 approaches:

1. Brute Force      → O(n³)
2. Better Approach  → O(n³) (cleaner logic)
3. Optimal Approach → O(n²) ✅ (best for interviews)

--------------------------------------------------
🧠 Problem:
Input:  "abba"
Output: "abba"

--------------------------------------------------
🚀 How to run:

👉 Command:
python palindrome.py
"""

# -----------------------------------------
# 🔹 1. BRUTE FORCE APPROACH
# -----------------------------------------
# Generate all substrings and check if palindrome

def brute_force(s):
    n = len(s)
    result = ""

    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]

            # check palindrome
            if sub == sub[::-1]:
                if len(sub) > len(result):
                    result = sub

    return result


# -----------------------------------------
# 🔹 2. BETTER APPROACH
# -----------------------------------------
# Instead of reversing string every time,
# check palindrome using two pointers

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def better(s):
    n = len(s)
    result = ""

    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s, i, j):
                if (j - i + 1) > len(result):
                    result = s[i:j+1]

    return result


# -----------------------------------------
# 🔹 3. OPTIMAL APPROACH (EXPAND AROUND CENTER)
# -----------------------------------------
# Idea:
# Every palindrome expands from its center
# Example:
# "aba" → center = b
# "abba" → center = bb

def optimal(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    result = ""

    for i in range(len(s)):
        # odd length palindrome
        p1 = expand(i, i)

        # even length palindrome
        p2 = expand(i, i+1)

        # update result
        if len(p1) > len(result):
            result = p1
        if len(p2) > len(result):
            result = p2

    return result


# -----------------------------------------
# 🔹 MAIN EXECUTION
# -----------------------------------------
if __name__ == "__main__":
    s = "abba"

    print("Input :", s)
    print("\n--- Results ---")

    print("Brute Force :", brute_force(s))
    print("Better      :", better(s))
    print("Optimal     :", optimal(s))


"""
--------------------------------------------------
📊 Complexity Summary

Brute Force  → O(n³)
Better       → O(n³)
Optimal      → O(n²) ✅

--------------------------------------------------
💡 Interview Tip:

If interviewer asks for best:
👉 Mention Manacher’s Algorithm (O(n))
👉 But implement Optimal (expand center)

--------------------------------------------------
"""