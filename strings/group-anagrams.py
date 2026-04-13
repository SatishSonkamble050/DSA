"""
Problem: Group Anagrams

Input:
["eat","tea","tan","ate","nat","bat"]

Output:
[
 ['eat', 'tea', 'ate'],
 ['tan', 'nat'],
 ['bat']
]
"""

import copy


# ------------------------------------------------------------
# 1.  BRUTE FORCE APPROACH
# ------------------------------------------------------------
def brute_force(strs):
    """
    Idea:
    - Compare each word with every other word
    - Use character frequency (hashmap) to check anagram
    - Time Complexity: O(n^2 * k)
    """

    hashmap = {}
    visited = set()   # To avoid duplicate grouping

    for i in range(len(strs)):
        if strs[i] in visited:
            continue

        hashmap[strs[i]] = [strs[i]]
        visited.add(strs[i])

        # Create frequency map for current word
        char_map = {}
        for ch in strs[i]:
            char_map[ch] = char_map.get(ch, 0) + 1

        # Compare with remaining words
        for j in range(i + 1, len(strs)):
            if strs[j] in visited:
                continue

            temp_map = copy.copy(char_map)
            flag = True

            for ch in strs[j]:
                if ch in temp_map:
                    temp_map[ch] -= 1
                else:
                    flag = False
                    break

            # Check if all counts are zero
            for val in temp_map.values():
                if val != 0:
                    flag = False
                    break

            if flag:
                hashmap[strs[i]].append(strs[j])
                visited.add(strs[j])

    return list(hashmap.values())


# ------------------------------------------------------------
# 2.  BETTER APPROACH (CHARACTER COUNT KEY)
# ------------------------------------------------------------
def better(strs):
    """
    Idea:
    - Use character frequency as key
    - Example: "eat" → [1,0,0,...,1,...]
    - Time Complexity: O(n * k)
    """

    hashmap = {}

    for word in strs:
        # Create 26-length array for a-z
        count = [0] * 26

        for ch in word:
            index = ord(ch) - ord('a')   # convert char → index
            count[index] += 1

        key = tuple(count)  # list can't be dict key → use tuple

        if key not in hashmap:
            hashmap[key] = []

        hashmap[key].append(word)

    return list(hashmap.values())


# ------------------------------------------------------------
# 3.  OPTIMAL APPROACH (SORTING)
# ------------------------------------------------------------
def optimal(strs):
    """
    Idea:
    - Sort each word → same sorted string = anagram
    - Example:
        eat → aet
        tea → aet
    - Time Complexity: O(n * k log k)
    """

    hashmap = {}

    for word in strs:
        key = "".join(sorted(word))  # sort characters

        if key not in hashmap:
            hashmap[key] = []

        hashmap[key].append(word)

    return list(hashmap.values())


# ------------------------------------------------------------
#  MAIN FUNCTION
# ------------------------------------------------------------
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("\n BRUTE FORCE RESULT:")
    print(brute_force(strs))

    print("\n BETTER RESULT:")
    print(better(strs))

    print("\n OPTIMAL RESULT:")
    print(optimal(strs))