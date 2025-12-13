from heapq import *

class Solution:
  def minimumCostToConnectRopes(self, ropeLengths):
    # TODO: Write your code here
    rope = []
    for ro in ropeLengths:
      heappush(rope, ro)

    tsum, temp = 0,0
    while len(rope) > 1:
      temp = heappop(rope) + heappop(rope)
      tsum += temp
      heappush(rope, temp)

    return tsum


def main():
  sol = Solution()
  print("Minimum cost to connect ropes: " +
        str(sol.minimumCostToConnectRopes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(sol.minimumCostToConnectRopes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(sol.minimumCostToConnectRopes([1, 3, 11, 5, 2])))

main()