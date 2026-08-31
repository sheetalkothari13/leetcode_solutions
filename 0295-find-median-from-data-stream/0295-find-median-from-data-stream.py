import heapq

class MedianFinder:

    def __init__(self):
        self.left = []    
        self.right = []   

    def addNum(self, num: int) -> None:
        if not self.right or num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right,-heapq.heappop(self.left))

        elif len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left,-heapq.heappop(self.right))

    def findMedian(self) -> float:

        if len(self.left) > len(self.right):
            return -self.left[0]

        elif len(self.right) > len(self.left):
            return self.right[0]

        else:
            return (-self.left[0] + self.right[0]) / 2