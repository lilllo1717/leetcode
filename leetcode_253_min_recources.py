from heapq import *

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x[0])
        # print(intervals)
        heapy = []

        for meeting in intervals:
            if not heapy or heapy[0] > meeting[0]:
                heappush(heapy, meeting[1])

            else:
                heapreplace(heapy, meeting[1])
        return len(heapy)

if __name__ == '__main__':
    sol = Solution()
    print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))