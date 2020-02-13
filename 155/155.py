# solution 1
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        currMin = self.getMin()
        if currMin is None or x < currMin:
            currMin = x
        self.stack.append((x, currMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]


# solution 2
class Node:
    def __init__(self, x, min, next):
        self.val = x
        self.currMin = min
        self.next = next


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, x):
        currMin = self.getMin()
        if currMin is None or x < currMin:
            currMin = x
        self.head = Node(x, currMin, self.head)

    def pop(self):
        topVal = self.head.val
        self.head = self.head.next
        return topVal

    def top(self):
        return self.head.val

    def getMin(self):
        return None if self.head is None else self.head.currMin
