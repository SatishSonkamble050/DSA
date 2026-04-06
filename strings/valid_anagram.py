"""
File: valid_anagram.py

Problem:
---------
Check if two strings are anagrams.

Definition:
-----------
Two strings are anagrams if they contain the same characters
with the same frequency but possibly in a different order.

Example:
--------
Input:  s = "anagram", t = "nagaram"
Output: True
"""

# ------------------------------------------------------------
# 1. BRUTE FORCE APPROACH
# ------------------------------------------------------------
def brute(str1: str, str2: str) -> bool:
    """
    Approach:
    ----------
    - Check length first
    - For each character in str1, find it in str2
    - Replace matched character with '0' (mark as used)

    Time Complexity: O(n^2) to O(n^3) (due to slicing)
    Space Complexity: O(n)
    """

    if len(str1) != len(str2):
        return False

    for ch in str1:
        found = False

        for j in range(len(str2)):
            if ch == str2[j]:
                # Strings are immutable → create new string
                str2 = str2[:j] + "0" + str2[j + 1:]
                found = True
                break

        if not found:
            return False

    # Check if all characters are matched
    for ch in str2:
        if ch != "0":
            return False

    return True


# ------------------------------------------------------------
# 2. SORTING APPROACH (BETTER)
# ------------------------------------------------------------
def best(str1: str, str2: str) -> bool:
    """
    Approach:
    ----------
    - Sort both strings
    - Compare sorted results

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """

    s1 = "".join(sorted(str1))
    s2 = "".join(sorted(str2))

    print(f"[DEBUG] Sorted s1: {s1}, Sorted s2: {s2}")

    return s1 == s2


# ------------------------------------------------------------
# 3. HASHMAP APPROACH (OPTIMAL)
# ------------------------------------------------------------
def optimize(str1: str, str2: str) -> bool:
    """
    Approach:
    ----------
    - Count frequency of characters using hashmap (dictionary)
    - Decrease count while traversing second string
    - If mismatch found → return False

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if len(str1) != len(str2):
        return False

    hashmap = {}

    # Step 1: Count characters in str1
    for ch in str1:
        print(f"[DEBUG] ASCII index of '{ch}':", ord(ch) - ord('a'))

        if ch in hashmap:
            hashmap[ch] += 1
        else:
            hashmap[ch] = 1

    print("[DEBUG] Frequency map after str1:", hashmap)

    # Step 2: Reduce count using str2
    for ch in str2:
        if ch not in hashmap:
            return False

        hashmap[ch] -= 1

        if hashmap[ch] == 0:
            del hashmap[ch]

    print("[DEBUG] Frequency map after str2:", hashmap)

    return len(hashmap) == 0


# ------------------------------------------------------------
# 4. ARRAY APPROACH (MOST OPTIMIZED)
# ------------------------------------------------------------
def optimize_array(str1: str, str2: str) -> bool:
    """
    Approach:
    ----------
    - Use fixed array of size 26 (for a–z)
    - Map character → index using ord()

    Formula:
        index = ord(character) - ord('a')

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if len(str1) != len(str2):
        return False

    count = [0] * 26

    for i in range(len(str1)):
        count[ord(str1[i]) - ord('a')] += 1
        count[ord(str2[i]) - ord('a')] -= 1

    print("[DEBUG] Final count array:", count)

    return all(c == 0 for c in count)


# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    print("\n--- BRUTE ---")
    print("Result:", brute(s, t))

    print("\n--- SORTING ---")
    print("Result:", best(s, t))

    print("\n--- HASHMAP ---")
    print("Result:", optimize(s, t))

    print("\n--- ARRAY (BEST) ---")
    print("Result:", optimize_array(s, t))