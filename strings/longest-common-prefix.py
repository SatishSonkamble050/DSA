"""
Longest Common Prefix (LCP) - All Approaches

Description:
This file contains multiple approaches to solve the
Longest Common Prefix problem.
"""


# -------------------------------
# 1. Brute Force Approach
# -------------------------------
def lcp_brute(strs):
    """
    Compare character by character across all strings
    """
    if not strs:
        return ""

    result = ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for word in strs:
            if i >= len(word) or word[i] != char:
                return result

        result += char

    return result


# -------------------------------
# 2. Better (Horizontal Scanning)
# -------------------------------
def lcp_horizontal(strs):
    """
    Take first word as prefix and shrink it
    """
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1

        prefix = prefix[:i]

        if prefix == "":
            return ""

    return prefix


# -------------------------------
# 3. Optimal (Sorting Trick)
# -------------------------------
def lcp_optimal(strs):
    """
    Sort array and compare first and last string
    """
    if not strs:
        return ""

    strs.sort()

    first = strs[0]
    last = strs[-1]

    i = 0
    while i < len(first) and first[i] == last[i]:
        i += 1

    return first[:i]


# -------------------------------
# Test Cases
# -------------------------------
if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interview", "internet", "internal"],
    ]

    for case in test_cases:
        print(f"\nInput: {case}")
        print("Brute      :", lcp_brute(case))
        print("Horizontal :", lcp_horizontal(case))
        print("Optimal    :", lcp_optimal(case))