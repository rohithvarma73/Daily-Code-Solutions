import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        # Function to compute the gain of adding a student
        def gain(p, t):
            return (p + 1) / (t + 1) - (p / t)

        # Max heap (store negative because Python has min-heap by default)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Assign extra students
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Compute final average ratio
        total = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t
        return total / len(classes)
