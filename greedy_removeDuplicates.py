from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # ToDo: Write Your Code Here.
        result = []
        hashMap = Counter(s)
        set_arr = set()
        for el in s:
            if el not in set_arr:
                while result and el < result[-1] and hashMap[result[-1]] > 0:
                    set_arr.remove(result.pop())
                result.append(el)
                set_arr.add(el)
            hashMap[el] -= 1

        return ''.join(result)

sol = Solution()
print(sol.removeDuplicateLetters("babac"))    # Output: "abc"
print(sol.removeDuplicateLetters("zabccde")) # Output: "zabcde"
print(sol.removeDuplicateLetters("mnopmn"))   # Output: "mnop"