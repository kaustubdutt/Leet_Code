class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        number = 0
        val = 9999
        len1 = len(s)
        for i in range(len1):
            if i == val:
                continue
            if i < len1 - 1:
                if numbers[s[i]] >= numbers[s[i+1]]:
                    number += numbers[s[i]]
                else:
                    number += (numbers[s[i+1]] - numbers[s[i]])
                    val = i + 1
            elif i == len1 - 1:
                if numbers[s[i]] <= numbers[s[i - 1]]:
                    number += numbers[s[i]]
        return number

solution = Solution()
fin = solution.romanToInt("MMMDCCCXCIX")
print(fin)





