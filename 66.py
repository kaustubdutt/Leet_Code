class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''.join(str(num) for num in digits)
        num1 = int(str1)
        num1 += 1
        num1 = str(num1)
        num_list = list(int(num) for num in num1)
        return num_list