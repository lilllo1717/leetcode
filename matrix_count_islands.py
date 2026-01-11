
class Solution:
  def countIslands(self, matrix):
    totalIslands = 0
    # TODO: Write your code here
    num_rows = len(matrix)
    num_col = len(matrix[0])
    for i in range(num_rows):
      for j in range(num_col):
        if matrix[i][j] == 1:
          totalIslands +=1
          self.countRecur(matrix, i, j)
    return totalIslands

  def countRecur(self, matrix, row, col):
    num_rows = len(matrix)
    num_col = len(matrix[0])
    if row >= num_rows or col >= num_col or col < 0 or row  < 0:
      return
    if matrix[row][col] == 0:
      return
    matrix[row][col] = 0
    self.countRecur(matrix, row + 1, col)
    self.countRecur(matrix, row - 1, col)
    self.countRecur(matrix, row, col + 1)
    self.countRecur(matrix, row, col - 1)


def main():
  sol = Solution()
  print(sol.countIslands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))
  print(sol.countIslands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))


main()
