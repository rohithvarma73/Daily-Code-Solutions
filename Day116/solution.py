class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compare two version strings and return:
        -1 if version1 < version2
        0 if version1 == version2
        1 if version1 > version2
        """
        # Get lengths of both version strings
        len1, len2 = len(version1), len(version2)
      
        # Initialize pointers for traversing both version strings
        ptr1 = ptr2 = 0
      
        # Continue comparing while at least one version has remaining segments
        while ptr1 < len1 or ptr2 < len2:
            # Initialize revision numbers for current segment
            revision1 = revision2 = 0
          
            # Parse the current revision number from version1
            # Continue until we hit a dot or reach the end
            while ptr1 < len1 and version1[ptr1] != '.':
                revision1 = revision1 * 10 + int(version1[ptr1])
                ptr1 += 1
          
            # Parse the current revision number from version2
            # Continue until we hit a dot or reach the end
            while ptr2 < len2 and version2[ptr2] != '.':
                revision2 = revision2 * 10 + int(version2[ptr2])
                ptr2 += 1
          
            # Compare current revision numbers
            if revision1 != revision2:
                return -1 if revision1 < revision2 else 1
          
            # Skip the dot separator and move to next segment
            ptr1 += 1
            ptr2 += 1
      
        # All revision segments are equal
        return 0