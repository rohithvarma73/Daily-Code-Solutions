class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = [i for i in range(26)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                if rootA < rootB:
                    parent[rootB] = rootA
                else:
                    parent[rootA] = rootB
        

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        
        result = []
        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            result.append(chr(root + ord('a')))
        
        return "".join(result)
