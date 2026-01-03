from collections import Counter

#ugliest solution ever:
class Solution:
    def largestPalindromic(self, num: str) -> str:
        # ToDo: Write Your Code Here.
        nums = sorted(num, reverse=True)
        new_list = Counter(nums)

        first = []
        second = []
        count_unique = 0
        letter = ""

        for key, val in new_list.items():
            if len(new_list) == 1 and key == "0":
                return "0"
            k = val // 2
            if val % 2 != 0 and count_unique == 0:
                count_unique = 1
                letter = key
            while k > 0:
                first.append(key)
                k -= 1
        j = 0

        while j < len(first) and first[j] == "0":
            j += 1
        first = first[j:]
        second.extend(first[::-1])

        if count_unique == 1:
            first.append(letter)
        if len(first) + len(second) == 1:
            return ''.join(first)
        for el in second:
            first.append(el)
        mew_string = ''.join(first)

        return mew_string[j:]

class Solution2:

    def largestPalindromic(self, s: str) -> str:
        firstHalf = []  # List to store first half of the palindrome
        frequency = [0] * 10  # Frequency array for digits 0-9

        # Count the frequency of each digit in the input number
        for ch in s:
            val = int(ch)
            frequency[val] += 1

        middle = -1  # Variable to store the middle digit if needed

        # Iterate from the highest digit (9) to the lowest (0)
        for i in range(9, -1, -1):
            if frequency[i] != 0 and (i != 0 or firstHalf):
                count = frequency[i]
                while count > 1:
                    firstHalf.append(str(i))  # Append the digit to firstHalf
                    count -= 2  # Use two of the digit for the first half
                if count == 1 and middle == -1:
                    middle = i  # Assign the middle digit if it's the largest odd-count digit

        secondHalf = firstHalf[::-1]  # Create secondHalf as a reversed copy of firstHalf
        if middle != -1:
            firstHalf.append(str(middle))  # Append the middle digit if it exists
        firstHalf.extend(secondHalf)  # Append the reversed first half to firstHalf

        return ''.join(firstHalf) if firstHalf else "0"  # Return the final palindrome or "0"


# Test cases
solution = Solution2()
print(solution.largestPalindromic("323211444"))  # 432141234
print(solution.largestPalindromic("998877"))      # 987789
print(solution.largestPalindromic("54321"))       # 5