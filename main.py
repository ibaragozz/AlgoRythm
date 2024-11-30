# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         return self.items == []
#
#     def peek(self):
#         return self.items[-1]
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.is_empty())
# print(stack.peek())

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)