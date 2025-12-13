from heapq import *


class Point:

 def __init__(self, x, y):
   self.x = x
   self.y = y

  # used for max-heap
 def __lt__(self, other):
   return self.distance_from_origin() > other.distance_from_origin()

 def distance_from_origin(self):
    # ignoring sqrt to calculate the distance
   return (self.x * self.x) + (self.y * self.y)

class Solution:
  def findClosestPoints(self, points, k):
    # print(type(points[0]))
    maxHeap = []

    for i in range(k):
      heappush(maxHeap, (-points[i].distance_from_origin(), points[i]))
    # for p in maxHeap:
    #   print(p[0], p[1])

    for i in range(k, len(points)):
      distance = -points[i].distance_from_origin()
      if distance > maxHeap[0][0]:
        heappop(maxHeap)
        heappush(maxHeap, (distance, points[i]))
    for p in maxHeap:
      print(p[0], p[1])
    final_points = []

    while maxHeap:
      final_points.append(maxHeap[0][1])
      heappop(maxHeap)

    return final_points

  @staticmethod
  def print_point(point):
    print("[" + str(point.x) + ", " + str(point.y) + "] ", end='')

def main():
  sol = Solution()
  result = sol.findClosestPoints([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest to the origin: ", end='')
  for point in result:
    Solution.print_point(point)  # Call the static method correctly


main()
