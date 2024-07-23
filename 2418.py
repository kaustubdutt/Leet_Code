from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = dict(zip(heights,names))
        sorted_dict = {key: result[key] for key in sorted(result, reverse=True)}
        print(sorted_dict)
        result_list = []
        for key in sorted_dict:
            result_list.append(sorted_dict[key])
        return result_list


solution = Solution()
result = solution.sortPeople(["Mary","John","Emma","Emma"],[180,165,181,200])
print(result)
