"""
===========================================================
String Compression - Brute Force, Better, and Optimized
===========================================================

Problem:
Given a list of characters, compress it in-place.

Example:
Input  = ["a","a","b","b","c","c","c"]
Output = ["a","2","b","2","c","3"]

-----------------------------------------------------------
1. Brute Force Approach
-----------------------------------------------------------

Idea:
- Traverse the array
- Count consecutive characters
- Store result in a separate list
- Return the new compressed list

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


def brute_force(chars):
    if not chars:
        return []

    result = []
    i = 0

    while i < len(chars):
        current_char = chars[i]
        count = 0

        while i < len(chars) and chars[i] == current_char:
            count += 1
            i += 1

        result.append(current_char)

        if count > 1:
            for digit in str(count):
                result.append(digit)

    return result


# Example
chars1 = ["a", "a", "b", "b", "c", "c", "c"]
print("Brute Force Output:", brute_force(chars1))


"""
-----------------------------------------------------------
2. Better Approach
-----------------------------------------------------------

Idea:
- Use two pointers
- Store compressed characters in a new array
- Slightly cleaner logic than brute force

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


def better(chars):
    if not chars:
        return []

    compressed = []
    left = 0

    while left < len(chars):
        right = left

        while right < len(chars) and chars[right] == chars[left]:
            right += 1

        count = right - left
        compressed.append(chars[left])

        if count > 1:
            compressed.extend(list(str(count)))

        left = right

    return compressed


# Example
chars2 = ["a", "a", "a", "b", "b", "c"]
print("Better Output:", better(chars2))


"""
-----------------------------------------------------------
3. Optimized Approach
-----------------------------------------------------------

Idea:
- Modify the original array in-place
- Use write pointer to overwrite characters
- Most memory efficient approach

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


def optimize(chars):
    write = 0
    i = 0

    while i < len(chars):
        char = chars[i]
        count = 0

        while i < len(chars) and chars[i] == char:
            i += 1
            count += 1

        chars[write] = char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return chars[:write]


# Example
chars3 = ["a", "a", "b", "b", "c", "c", "c"]
print("Optimized Output:", optimize(chars3))


"""
===========================================================
Example Outputs
===========================================================

Input:
["a","a","b","b","c","c","c"]

Brute Force Output:
['a', '2', 'b', '2', 'c', '3']

Better Output:
['a', '3', 'b', '2', 'c']

Optimized Output:
['a', '2', 'b', '2', 'c', '3']
===========================================================
"""