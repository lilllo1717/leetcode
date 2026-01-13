class Solution:
    def nthUglyNumber(self, n) :

        min_heap  = [1]
        el1_indx = 0
        el2_indx = 0
        el3_indx = 0

        # array [1,    some*2 || some*3 || some*5,   some*2 || some*3 || some*5 .... nth]
        for i in range(n - 1):
            first_opt = min_heap[el1_indx] * 2
            second_opt = min_heap[el2_indx] * 3
            third_opt = min_heap[el3_indx] * 5
            el_to_add = min(first_opt, second_opt, third_opt)
            min_heap.append(el_to_add)

            if el_to_add%2 == 0:
                el1_indx +=1
            if el_to_add%3==0:
                el2_indx += 1
            if el_to_add%5 == 0:
                el3_indx +=1

        print(min_heap)
        return (min_heap[-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(10))
