class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        transformed = [1 if num % 2 != 0 else 0 for num in nums]
        prefix_sum = 0
        count = 0
        prefix_counts = {0: 1}

        for num in transformed:
            prefix_sum += num
            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]

            if prefix_sum in prefix_counts:
                prefix_counts[prefix_sum] += 1
            else:
                prefix_counts[prefix_sum] = 1

        return count

