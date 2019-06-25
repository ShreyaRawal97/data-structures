class DoubleNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

#Implement a doubly linked list that can append to the tail in constant time.
#Make sure to include forward and backward connections when adding a new node to the list.

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        # TODO: Implement this method to append to the tail of the list
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

# Test your class here

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
