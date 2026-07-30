class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        averages = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)

            averages.append([dist, x, y])
        heapq.heapify(averages)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(averages)
            res.append([x, y])
            k -= 1
        return res

