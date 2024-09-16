class Solution:
    def nearestPalindromic(self, n: str) -> str:
        K = len(n)
        candidates = [str(10**K + 1), str(10**(K - 1) - 1)]
        prefix = n[:(K + 1) // 2]
        for start in map(str, [int(prefix) - 1, int(prefix), int(prefix) + 1]):
            candidates.append(start + (start[:-1] if K % 2 else start)[::-1])

        def diff(x):
            return abs(int(x) - int(n))

        ans = min((c for c in candidates if c != n), key=diff)
        return ans
sol = Solution()
answer = sol.nearestPalindromic("11399")
print(answer)
