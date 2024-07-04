class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9

'''digital root is the forumala used above it is  described as above ((number - 1) % 9) + 1'''

solution = Solution()
result = solution.addDigits(77)
print(result)