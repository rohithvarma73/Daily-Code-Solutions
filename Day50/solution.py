import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort()
        
        # Min heap to store end days of currently available events
        min_heap = []
        
        # Find the range of days we need to consider
        max_day = max(event[1] for event in events)
        
        count = 0
        event_idx = 0
        
        # Process each day from 1 to max_day
        for day in range(1, max_day + 1):
            # Add all events that start on this day to the heap
            while event_idx < len(events) and events[event_idx][0] == day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1
            
            # Remove events that have already ended (end day < current day)
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # If there are available events, attend the one that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                count += 1
        
        return count