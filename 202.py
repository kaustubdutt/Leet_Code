class Solution:
    def isHappy(self, n: int) -> bool:
        sq = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 0: 0}
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            summation = sum(sq[int(digit)] for digit in str(n))
            if summation == 1:
                return True
            else:
                n = summation
                print(summation)
        return True

solution = Solution()
fin = solution.isHappy(44)
print(fin)