class Solution:
    def largestTriangleArea(self, points):
        
        n = len(points)
        best = 0.0
        #shoelace formula

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area2 = abs((x2-x1)*(y3 - y1) - (y2-y1)*(x3-x1))
                    if area2 > best:
                        best = area2

        return best/2.0


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
