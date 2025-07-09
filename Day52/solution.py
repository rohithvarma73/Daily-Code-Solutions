from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        # Step 1: Create a list of all consecutive segments (gaps and meetings)
        # Each segment is represented by its duration.
        # We also need to know if a segment is a 'gap' or a 'meeting' to apply the 'k' budget.
        # Even indices (0, 2, 4...) in 'segments' will represent gaps.
        # Odd indices (1, 3, 5...) in 'segments' will represent meetings.
        
        segments = []

        # Initial free time before the first meeting: [0, startTime[0]]
        segments.append(startTime[0] - 0) 

        for i in range(n):
            # Meeting duration: [startTime[i], endTime[i]]
            segments.append(endTime[i] - startTime[i])
            
            # Gap after meeting i (if it's not the last meeting): [endTime[i], startTime[i+1]]
            if i < n - 1:
                segments.append(startTime[i+1] - endTime[i])
        
        # Final free time after the last meeting: [endTime[n-1], eventTime]
        segments.append(eventTime - endTime[n-1])

        # Step 2: Use a sliding window to find the longest continuous period of free time.
        # The window tracks a contiguous block of segments.
        # 'current_free_in_window' will sum the durations of only the 'gap' segments within the window.
        # 'meetings_in_window' will count the 'meeting' segments within the window.
        
        max_free_time = 0
        current_free_in_window = 0
        meetings_in_window = 0  # Counter for meetings within the current window
        left = 0                # Left pointer of the sliding window

        for right in range(len(segments)):
            segment_duration = segments[right]

            # Check if the current segment is a gap (even index) or a meeting (odd index)
            # 0-indexed: index 0 (gap), 1 (meeting), 2 (gap), 3 (meeting), ...
            if right % 2 == 0:  # It's a gap segment
                current_free_in_window += segment_duration
            else:  # It's a meeting segment
                meetings_in_window += 1 # This meeting costs 1 budget if kept in the window's span.
                                        # Its duration does NOT add to free_time, as it's assumed rescheduled.

            # If the number of meetings in the current window exceeds our budget 'k',
            # we need to shrink the window from the left.
            while meetings_in_window > k:
                left_segment_duration = segments[left]

                # Check if the segment being removed from the left is a gap or a meeting.
                if left % 2 == 0:  # It's a gap segment
                    current_free_in_window -= left_segment_duration
                else:  # It's a meeting segment
                    meetings_in_window -= 1 # This meeting is no longer counted towards the budget for this window.
                                            # Its duration was never added to current_free_in_window.
                left += 1

            # After ensuring 'meetings_in_window <= k', the 'current_free_in_window'
            # represents a valid continuous free time period that can be achieved.
            # Update the maximum found so far.
            max_free_time = max(max_free_time, current_free_in_window)

        return max_free_time