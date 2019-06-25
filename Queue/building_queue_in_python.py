#queue is a data structure that consists of two main operations: enqueue and dequeue
#enqueue is when you add an element to the tail of the queue
# and a pop is when you remove an element from the head of the queue

class Queue:
    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        return self.storage.pop(0)

#Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

#test size
pring("pass" if (q.size() == 3) else "Fail")

#test dequeue
print("pass" if (q.dequeue() == 1) else "Fail")

#Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
