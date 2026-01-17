from collections import Counter, OrderedDict
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

    def frequencySort2(self, s):
        mp = Counter(s)
        r = OrderedDict(sorted(mp.items(), key=lambda x: x[1], reverse=True))
        ss = ''.join([char * freq for char, freq in r.items()])
        return ss


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort2("cccaaa"))