class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        words = {'b' : 0 , 'a' : 0 , 'l' : 0 , 'o' : 0 , 'n' : 0 }
        for char in text:
            if char in words:
                words[char] += 1
            else:
                continue
        words['o'] //= 2
        words['l'] //= 2
        return min(words.values())
