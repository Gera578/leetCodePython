class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([s1 + s2 for s1, s2 in zip(word1 + ' '*len(word2), word2 + ' '*len(word1))]).replace(' ', '')

conc: Solution = Solution()
print(conc.mergeAlternately('abcd', 'pqr'))