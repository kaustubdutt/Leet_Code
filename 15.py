from typing import List
class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        numbers.sort()
        length = len(numbers)
        triplets = []

        for index in range(length - 2):
            if index > 0 and numbers[index] == numbers[index - 1]:
                continue

            start = index + 1
            end = length - 1
            while start < end:
                current_sum = numbers[index] + numbers[start] + numbers[end]
                if current_sum < 0:
                    start += 1
                elif current_sum > 0:
                    end -= 1
                else:
                    triplets.append([numbers[index], numbers[start], numbers[end]])
                    while start < end and numbers[start] == numbers[start + 1]:
                        start += 1
                    while start < end and numbers[end] == numbers[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1

        return triplets
sol = Solution()
fin = sol.threeSum([-1,0,1,0])
print(fin)

