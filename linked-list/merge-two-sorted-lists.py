"""
Merge Two Sorted Linked Lists
=============================

This file contains three approaches:

1. Brute Force (Using Array)
2. Better Approach (Iterative Merge)
3. Optimal Approach (Recursive)

Author: Sateesh Sonkamble
"""

# -----------------------------
# Node Definition
# -----------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# -----------------------------
# Utility Function
# -----------------------------
def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


# ============================================================
# 1️⃣ Brute Force Approach (Using Array)
# ============================================================
def merge_bruteforce(l1, l2):
    """
    Convert linked lists to array, sort, rebuild list.

    Time Complexity: O((n+m) log(n+m))
    Space Complexity: O(n+m)
    """
    arr = []

    while l1:
        arr.append(l1.data)
        l1 = l1.next

    while l2:
        arr.append(l2.data)
        l2 = l2.next

    arr.sort()

    dummy = Node(-1)
    temp = dummy

    for val in arr:
        temp.next = Node(val)
        temp = temp.next

    return dummy.next

# -----------------------------
# Better Approach (Recursive)
# -----------------------------
def merge_better(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.data < l2.data:
        l1.next = merge_better(l1.next, l2)
        return l1
    else:
        l2.next = merge_better(l1, l2.next)
        return l2
    
    


# -----------------------------
# Optimal Approach (Iterative)
# -----------------------------
def merge_optimal(l1, l2):
    dummy = Node(-1)
    prev = dummy

    while l1 and l2:
        if l1.data < l2.data:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    if l1:
        prev.next = l1
    else:
        prev.next = l2

    return dummy.next





# ============================================================
# Example Usage
# ============================================================
if __name__ == "__main__":
    # List 1: 10 -> 30 -> 50
    n1 = Node(10)
    n3 = Node(30)
    n5 = Node(50)

    n1.next = n3
    n3.next = n5
    l1 = n1

    # List 2: 20 -> 40
    n2 = Node(20)
    n4 = Node(40)

    n2.next = n4
    l2 = n2

    print("List 1:")
    display(l1)

    print("List 2:")
    display(l2)

    print("\nBrute Force:")
    display(merge_bruteforce(l1, l2))

    # recreate lists (since nodes are reused)
    n1.next = n3
    n3.next = n5
    n2.next = n4

    print("\nBetter (Iterative):")
    display(merge_better(l1, l2))

    # recreate again
    n1.next = n3
    n3.next = n5
    n2.next = n4

    print("\nOptimal (Recursive):")
    display(merge_optimal(l1, l2))