class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_palindrome = ""
        for i in range(len(s)):
            odd_palindrome = expand_around_center(s, i, i)
            if len(odd_palindrome) > len(max_palindrome):
                max_palindrome = odd_palindrome

            even_palindrome = expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(max_palindrome):
                max_palindrome = even_palindrome

        return max_palindrome
solution = Solution()
result = solution.longestPalindrome("cccc")
print(result)





