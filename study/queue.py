#!/usr/bin/env python3
import string, random
class QueueException(Exception):
    def __init__(self, message, exit_code):
        self.exit = exit_code
        self.message = message
        print(self.message)
        exit(self.exit)
class Queue(object):
    def __init__(self, size: int):
        self.size = size
        self.array = []
    def enqueue(self, message: str):
        if len(self.array) == self.size:
            raise QueueException("size of the queue is reached", 1)
        self.array.append(message)
    def dequeue(self):
        if len(self.array) == 0:
            raise QueueException("size of the queue is reached", 2)
        dequeued_message = self.array.pop(0)
        return dequeued_message
test = Queue(101)
test_data = []
def gen(size: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
for i in range(100):
    test_data.append(gen(15))
for message in test_data:
    test.enqueue(message)
for i in range(100):
    print(test.dequeue())