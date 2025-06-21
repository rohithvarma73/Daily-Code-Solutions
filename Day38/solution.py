from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1
        frequencies = sorted(freq.values())
        min_deletions = float('inf')
        
        for i in range(len(frequencies)):
            target = frequencies[i]
            deletions = 0
            for j in range(len(frequencies)):
                if j < i:
                    # frequencies[j] must be increased to target (but we can't, so delete all)
                    deletions += frequencies[j]
                else:
                    # frequencies[j] can be at most target + k
                    if frequencies[j] > target + k:
                        deletions += frequencies[j] - (target + k)
            min_deletions = min(min_deletions, deletions)
        
        return min_deletions