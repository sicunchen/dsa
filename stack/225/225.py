# https://leetcode.com/problems/implement-stack-using-queues/


from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    # 将queue1中元素移入queue2,留下最后一个。
    def moveItems(self):
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())

    def swapQueues(self):
        self.queue1, self.queue2 = self.queue2, self.queue1

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        self.moveItems()
        popped = self.queue1.popleft()
        self.swapQueues()
        return popped

    def top(self):
        self.moveItems()
        item = self.queue1.popleft()
        self.swapQueues()
        self.queue1.append(item)
        return item

    def empty(self):
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
