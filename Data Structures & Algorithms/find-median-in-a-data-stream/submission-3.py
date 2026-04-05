class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)
        elif - num > self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        diff_len = len(self.small) - len(self.large)
        if diff_len > 1:
            el = - heapq.heappop(self.small)
            heapq.heappush(self.large, el)
        elif diff_len < -1:
            el = heapq.heappop(self.large)
            heapq.heappush(self.small, -el)


        

    def findMedian(self) -> float:
        diff_len = len(self.small) - len(self.large)
        if diff_len == 0:
            return (self.large[0] - self.small[0]) / 2
        elif diff_len > 0:
            return - self.small[0]
        else:
            return self.large[0]
        