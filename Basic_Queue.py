from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, item):
        self.queue.append(item)
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("dequeue from an empty queue")
    def print_queue(self):
        print("Queue contents:", list(self.queue))
items = input("Enter elements separated by space: ").split()
q = Queue()
for item in items:
    q.enqueue(item)
q.print_queue()
