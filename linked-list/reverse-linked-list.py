# linked_list_reverse.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def display(head):
    """
    Prints the linked list.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


# -------------------------------
# 1. Brute Force Approach
# -------------------------------
def reverse_bruteforce(head):
    """
    Reverse linked list by storing values in a list and reassigning.

    Steps:
    1. Store all node values in a list
    2. Traverse again and assign reversed values

    Time Complexity: O(n)
    Space Complexity: O(n)  # extra list used
    """
    values = []
    temp = head

    while temp:
        values.append(temp.data)
        temp = temp.next

    temp = head
    while temp:
        temp.data = values.pop()
        temp = temp.next

    return head


# -------------------------------
# 2. Stack Approach
# -------------------------------
def reverse_stack(head):
    """
    Reverse linked list using stack (LIFO).

    Steps:
    1. Push all nodes into stack
    2. Pop nodes and reconnect

    Time Complexity: O(n)
    Space Complexity: O(n)  # stack used
    """
    stack = []
    temp = head

    while temp:
        stack.append(temp)
        temp = temp.next

    head = stack.pop()
    temp = head

    while stack:
        node = stack.pop()
        temp.next = node
        temp = temp.next

    temp.next = None
    return head


# -------------------------------
# 3. Optimal Approach
# -------------------------------
def reverse_optimal(head):
    """
    Reverse linked list by changing pointers in-place.

    Steps:
    1. Maintain prev, current, next pointers
    2. Reverse links one by one

    Time Complexity: O(n)
    Space Complexity: O(1)  # no extra memory used
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# -------------------------------
# Driver Code
# -------------------------------
if __name__ == "__main__":
    # Create linked list: 10 -> 20 -> 30
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)

    head = n1
    n1.next = n2
    n2.next = n3

    print("Original:")
    display(head)

    print("\nBrute Force:")
    display(reverse_bruteforce(head))

    # Recreate list
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    head = n1
    n1.next = n2
    n2.next = n3

    print("\nStack Approach:")
    display(reverse_stack(head))

    # Recreate list
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    head = n1
    n1.next = n2
    n2.next = n3

    print("\nOptimal Approach:")
    head = reverse_optimal(head)
    display(head)