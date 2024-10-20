class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = "0"
        for i in range(1,n+1):
            inv_S = ['1' if bit == '0' else '0' for bit in S]
            inv_S = inv_S[::-1]
            inv_S = ''.join(inv_S)
            S = S + "1" + inv_S
        return S[k-1]