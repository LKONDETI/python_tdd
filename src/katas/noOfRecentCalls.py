from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.cnt = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.cnt += 1

        while self.q and self.q[0] < t-3000:
            self.q.popleft()
            self.cnt-= 1
        
        return self.cnt