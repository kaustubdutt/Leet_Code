class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_val = {}
        for i,num in enumerate(nums):
            compliment = target - num;
            if compliment in num_val:
                return [i,num_val[compliment]]
                break
            else:
                num_val[num] = i
        return []