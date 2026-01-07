from heapq import *

class Solution:
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        min_heap = []
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        for id, rep in zip(student_id, report):
            score = 0
            words = rep.lower().split()
            for word in words:
                if word in pos:
                    score +=3
                elif word in neg:
                    score -=1
            heappush(min_heap, (-score, id))

        result = []
        for i in range(k):
            result.append(heappop(min_heap)[1])
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.topStudents(["smart","brilliant","studious"], ["not"], ["this student is studious","the student is smart"], [1,2], 2))