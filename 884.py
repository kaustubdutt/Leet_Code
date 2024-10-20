from typing import List
class Solution:
    class Solution:
        def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
            s1 = s1.split(" ")
            s2 = s2.split(" ")
            dict1 = {}
            dict2 = {}
            for word in s1:
                if word in dict1:
                    dict1[word] += 1
                else:
                    dict1[word] = 1

            for word in s2:
                if word in dict2:
                    dict2[word] += 1
                else:
                    dict2[word] = 1

            print(dict2)

            result = []
            for key, value in dict1.items():
                if dict1[key] == 1 and key not in dict2:
                    result.append(key)

            for key, value in dict2.items():
                if dict2[key] == 1 and key not in dict1:
                    result.append(key)

            return result





sol = Solution()
answer = sol.uncommonFromSentences("this apple is sweet sweet","this apple is sour")
print(answer)