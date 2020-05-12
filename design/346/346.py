# https://leetcode.com/problems/moving-average-from-data-stream/


class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.sum = 0
        self.queue = collections.deque([])

    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        # write your code here
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)

