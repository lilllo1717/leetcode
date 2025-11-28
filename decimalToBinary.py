class Solution: 
    def decimalToBinary(self, num):
        # ToDo: Write Your Code Here.
        binary = []
        printy = []
        while num > 0:
            binary.append(num%2)
            num = num//2
        # print(binary)
        while binary:
            printy.append(str(binary.pop()))
        return ''.join(printy)


def main():
    sol = Solution()
    res = sol.decimalToBinary(7)
    res2 = sol.decimalToBinary(11)

    print(res)
    print(res2)


main()