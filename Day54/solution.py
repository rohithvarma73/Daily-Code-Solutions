from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
      
        # Initialize a heap for tracking busy rooms and idle rooms
        busy_rooms_heap = []
        idle_rooms_heap = list(range(n))
        heapify(idle_rooms_heap)
      
        # Initialize a counter to track number of meetings for each room
        meeting_count = [0] * n
      
        # Iterate over sorted meetings
        for start_time, end_time in meetings:
            # Free up rooms that have finished their meeting before current meeting starts
            while busy_rooms_heap and busy_rooms_heap[0][0] <= start_time:
                room_index = heappop(busy_rooms_heap)[1]
                heappush(idle_rooms_heap, room_index)
          
            # If there's an idle room, use it
            if idle_rooms_heap:
                room_index = heappop(idle_rooms_heap)
                meeting_count[room_index] += 1
                heappush(busy_rooms_heap, (end_time, room_index))
            else:
                # No idle rooms; wait for the first available room
                earliest_end, room_index = heappop(busy_rooms_heap)
                meeting_count[room_index] += 1
              
                # Schedule the meeting in the now available room and push it back onto the busy heap
                heappush(busy_rooms_heap, (earliest_end + end_time - start_time, room_index))
      
        # Find the room with the most meetings booked
        most_booked_room = 0
        
        for i, count in enumerate(meeting_count):
            if meeting_count[most_booked_room] < count:
                most_booked_room = i
              
        return most_booked_room