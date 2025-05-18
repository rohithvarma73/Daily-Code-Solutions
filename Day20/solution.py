from functools import lru_cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        # Generate all valid column colorings
        def generate_valid_columns():
            def dfs(path):
                if len(path) == m:
                    valid_columns.append(tuple(path))
                    return
                for color in [0, 1, 2]:  # 0: red, 1: green, 2: blue
                    if not path or color != path[-1]:
                        dfs(path + [color])

            valid_columns = []
            dfs([])
            return valid_columns

        # Generate transitions between columns
        def generate_transitions(valid_columns):
            transitions = {col: [] for col in valid_columns}
            for a in valid_columns:
                for b in valid_columns:
                    if all(x != y for x, y in zip(a, b)):
                        transitions[a].append(b)
            return transitions

        valid_columns = generate_valid_columns()
        transitions = generate_transitions(valid_columns)

        @lru_cache(None)
        def dp(col_idx, prev_col):
            if col_idx == n:
                return 1
            total = 0
            for next_col in transitions[prev_col]:
                total = (total + dp(col_idx + 1, next_col)) % MOD
            return total

        total_ways = 0
        for col in valid_columns:
            total_ways = (total_ways + dp(1, col)) % MOD

        return total_ways
