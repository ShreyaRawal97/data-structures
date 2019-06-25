#Create and initialize the Stack class
class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0 #keeps track of what the top of the stack is
        self.num_elements = 0

    #Add the push method (add elements to the top of the stack)
    def push(self, data):
        if self.next_index == len(self.arr):
            print("out of space. increasing array capacity...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    #Add the pop method
    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    #Add the size method (returns current size of the stack)
    def size(self):
        return self.num_elements

    #Add the is_empty method (if stack is empty return True)
    def is_empty(self):
        if self.num_elements == 0:
            return True
        return False

    #Handle full capacity (to avoid index out of range error)
    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2* len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

foo = Stack()
print(foo.size()) # Should return 0
print(foo.is_empty()) # Should return True
foo.push("Test") # Let's push an item onto the stack and check again
print(foo.size()) # Should return 1
print(foo.is_empty()) # Should return False
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10) # The array is now at capacity!
foo.push(11) # This one should cause the array to increase in size
print(foo.arr) # Let's see what the array looks like now!
print("Pass" if len(foo.arr) == 20 else "Fail") # If we successfully doubled the array size, it should now be 20.
