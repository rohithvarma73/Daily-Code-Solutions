class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        def get_distances(start):
            dist = {}
            d = 0
            while start != -1 and start not in dist:
                dist[start] = d
                start = edges[start]
                d += 1
            return dist
        
        # Get distances from node1 and node2
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        # Find node reachable from both, with minimum max distance
        min_dist = float('inf')
        answer = -1
        for i in range(len(edges)):
            if i in dist1 and i in dist2:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist or (max_dist == min_dist and i < answer):
                    min_dist = max_dist
                    answer = i
        return answer
