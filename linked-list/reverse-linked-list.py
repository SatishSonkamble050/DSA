class Node:
   def __init__(self, data):
        self.data = data
        self.next = None

def display(head):
    temp = head

    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None")

def reverser(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    display(prev)


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

head = n1
n1.next = n2
n2.next = n3

display(head)
reverser(head)

