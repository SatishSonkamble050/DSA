"""
Linked List Cycle Detection
==========================

This file demonstrates three approaches to detect a cycle in a singly linked list:

1. Brute Force (Using Hashing)
2. Better Approach (Set Optimization)
3. Optimal Approach (Floyd’s Cycle Detection - Tortoise & Hare)

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
    """
    Prints the linked list (Only for non-cyclic lists)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


# ============================================================
# 1️⃣ Brute Force Approach (Using List / Visited Tracking)
# ============================================================
def has_cycle_bruteforce(head):
    """
    Detect cycle using a list to store visited nodes.

    Logic:
    - Traverse the list
    - Store each node in a list
    - If a node repeats → cycle exists

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    visited = []

    temp = head
    while temp:
        if temp in visited:
            return True
        visited.append(temp)
        temp = temp.next

    return False


# ============================================================
# 2️⃣ Better Approach (Using Set)
# ============================================================
def has_cycle_better(head):
    """
    Detect cycle using a hash set.

    Logic:
    - Store visited nodes in a set (O(1) lookup)
    - If node already exists → cycle

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    visited = set()

    temp = head
    while temp:
        if temp in visited:
            return True
        visited.add(temp)
        temp = temp.next

    return False


# ============================================================
# 3️⃣ Optimal Approach (Floyd’s Cycle Detection)
# ============================================================
def has_cycle_optimal(head):
    """
    Detect cycle using two pointers (slow & fast).

    Logic:
    - Slow moves 1 step
    - Fast moves 2 steps
    - If they meet → cycle exists

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# ============================================================
# Example Usage
# ============================================================
if __name__ == "__main__":
    # Creating nodes
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)

    # Linking nodes
    head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    # Create cycle
    n4.next = n2

    print("Brute Force:", has_cycle_bruteforce(head))
    print("Better (Set):", has_cycle_better(head))
    print("Optimal (Floyd):", has_cycle_optimal(head))