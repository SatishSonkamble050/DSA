class Node():
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList():
    def __init__(self):
        self.head = None
   
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        # if self.head is None:
        #     self.head = new_node
        #     return

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        count = 0

        while temp is not None and count < position-1:
            temp = temp.next
            count += 1
        
        if temp is None:
            print("Position out of range")
            return
        
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print("None")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        # print("RESVERSE : ", prev)

        # 10 => 20 => 30
        # 20=>10=>30
        # 30=>20=>10



l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.insert_at_position(100, 2)
l1.prepend(50)


l1.display()


l1.reverse()
l1.display()