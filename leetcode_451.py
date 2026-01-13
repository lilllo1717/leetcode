from collections import Counter
from heapq import *

class Solution:
    def frequencySort(self, s):
        count_chars = Counter(s)
        print(count_chars)
        result = []
        final = []

        for key, val in count_chars.items():
            heappush(result, (-val, key))
        # print("result", result)
        while result:
            # print(el)
            temp = heappop(result)
            # print(temp)
            final.append(temp[1] * -temp[0])
        # print(final)
        return ''.join(final)


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort("cccaaa"))