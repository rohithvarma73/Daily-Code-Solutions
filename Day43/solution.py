class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        # We will try possible lengths from the maximum possible down to 1
        max_possible_len = n // k
        for L in range(max_possible_len, 0, -1):
            # We need to find a subsequence of length L, repeated k times is a subsequence of s
            candidates = self.generate_candidates(s, L, k)
            if candidates:
                return max(candidates)
        return ""
    
    def generate_candidates(self, s, L, k):
        # This function generates all possible subsequences of length L that when repeated k times are a subsequence of s
        # But generating all possible is infeasible for large L, so we need a smarter way
        # Instead, we can perform a BFS approach, building the candidate character by character, checking feasibility
        from collections import deque
        possible_sequences = deque()
        possible_sequences.append("")
        for _ in range(L):
            next_level = set()
            for seq in possible_sequences:
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_seq = seq + c
                    if self.is_possible(s, new_seq, k):
                        next_level.add(new_seq)
            if not next_level:
                return []
            possible_sequences = deque(sorted(next_level, reverse=True))  # to process lex larger first
        return list(possible_sequences)
    
    def is_possible(self, s, seq, k):
        target = seq * k
        it = iter(s)
        return all(c in it for c in target)