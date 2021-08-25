# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


class Queue:
    def __init__(self):
        self.main_stack = list()
        self.aux_stack = list()

    def __repr__(self):
        return str(self.main_stack)

    def enqueue(self, val):
        self.main_stack.append(val)

    def dequeue(self):
        if not self.main_stack:
            return None

        while self.main_stack:
            self.aux_stack.append(self.main_stack.pop())
        val = self.aux_stack.pop()
        while self.aux_stack:
            self.main_stack.append(self.aux_stack.pop())
        return val