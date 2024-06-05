class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack limit reached")

    def pop(self):
        if self.isEmpty():
            return None  # Return None instead of raising an error
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None  # Return None instead of raising an error
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            # Find the 1-based position of the target from the top of the stack
            index = self.items[::-1].index(target)
            return index
        except ValueError:
            return -1
