class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_Dict = {}
        magazine_Dict = {}
        for char in ransomNote:
            if char in ransomNote_Dict:
                ransomNote_Dict[char] += 1
            else:
                ransomNote_Dict[char] = 1
        for char1 in magazine:
            if char1 in magazine_Dict:
                magazine_Dict[char1] += 1
            else:
                magazine_Dict[char1] = 1

        result = False

        for key in ransomNote_Dict:
            if key in magazine_Dict:
                if  magazine_Dict[key] >= ransomNote_Dict[key]:
                    print("True",key)
                    result = True
                else:
                    print("second false")
                    result = False
                    break
            else:
                result = False
                break
        return result
solution = Solution()
fin = solution.canConstruct("ihgg","ch")
print(fin)
