class RecentCounter:

    def __init__(self):
        self.deque=collections.deque([])

    def ping(self, t: int) -> int:
        if len(self.deque)<1:
            self.deque.append(t)
            return len(self.deque)
        else:
            while self.deque and t-self.deque[0]>3000:
                self.deque.popleft()
            self.deque.append(t)
            return len(self.deque)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
