
from heapq import *
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        # counts = list(Counter(tasks).values())
        # most_repeat = max(counts)
        # num_long = counts.count(most_repeat)
        # return max(len(tasks), (most_repeat-1) + (n+1) + num_long)
        counter = Counter(tasks)
        max_heap = []
        for key, val in counter.items():
            heappush(max_heap, (-val, key))
        time = 0

        while max_heap:
            tmp = []
            for i in range(n + 1):
                if max_heap:
                    tmp.append(heappop(max_heap))
            for key, val in tmp:
                if key+1 < 0:
                    heappush(max_heap, (key+1, val))

            time += len(tmp)  if not max_heap else n+1

        return time
if __name__ == '__main__':
    sol = Solution()
    print(sol.leastInterval(["A","A","A","B","B","B"], 2))