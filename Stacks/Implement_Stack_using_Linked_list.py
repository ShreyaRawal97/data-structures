#The time complexity of stacks using linked lists is better than
# an array.
# With the linked list implementation, pop and push have a time
# complexity of O(1).
# There is also no issue with handling space with the linked list implementation.


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0

    def push(self, value):
        new_node = Node(value)

        #if stack is empty
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    #add the pop method.
    def pop(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    # TODO: Add the size method
    def size(self):
        return self.num_elements

    # TODO: Add the is_empty method
    def is_empty(self):
        if self.num_elements == 0:
            return True
        return False

# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")
