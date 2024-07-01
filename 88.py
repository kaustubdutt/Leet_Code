from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
                print("if")
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
                print("else")


        while p1 < 0 and p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
            print("other loop")
        print(nums1)



solution = Solution()
result = solution.merge([0,0,0,0,0,0], 0, [2,2,3,4,5,6], 6)
print(result)
