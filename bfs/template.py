from collections import deque

# 无需分层遍历
def bfs(start):
    queue = deque()
    seen = set()

    seen.add(start)
    queue.append(start)

    while len(queue):
        head = queue.popleft()
        for neighbor in head.neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)


# 需要分层遍历，比如binary tree level order traversal
# for loop 的目的： https://www.jiuzhang.com/qa/7981/
def bfs2(start):
    queue = deque()
    seen = set()

    seen.add(start)
    queue.append(start)

    while len(queue):
        size = len(queue)
        for _ in range(size):
            head = queue.popleft()
            for neighbor in head.neighbors:
                seen.add(neighbor)
                queue.append(neighbor)
