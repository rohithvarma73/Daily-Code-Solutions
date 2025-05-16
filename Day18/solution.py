from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n              # dp[i] = length of longest valid subsequence ending at i
        prev = [-1] * n           # to reconstruct the path
        
        # Helper to compute Hamming Distance
        def hamming_distance(w1: str, w2: str) -> int:
            return sum(a != b for a, b in zip(w1, w2))
        
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if hamming_distance(words[i], words[j]) == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j
        
        # Find the index of the max dp value
        max_len = max(dp)
        idx = dp.index(max_len)
        
        # Reconstruct the path
        res = []
        while idx != -1:
            res.append(words[idx])
            idx = prev[idx]
        
        return res[::-1]  # reverse to get the correct order