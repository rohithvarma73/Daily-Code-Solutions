class Solution:
  def maxFreeTime(
      self,
      eventTime: int,
      startTime: list[int],
      endTime: list[int]
  ) -> int:
    '''
    Calculates the maximum continuous free time that can be achieved
    by rescheduling at most one meeting within the event duration.

    Parameters:
    - eventTime: total time of the event (e.g., 10 means [0,10])
    - startTime: list of meeting start times
    - endTime: list of meeting end times

    Returns:
    - Maximum free time achievable
    '''

    n = len(startTime)  # Total number of meetings

    '''
    Compute all the gaps (free time) between meetings:
    - First gap is from 0 to startTime[0]
    - Middle gaps are between end[i-1] and start[i]
    - Last gap is from endTime[-1] to eventTime
    '''
    gaps = (
      [startTime[0]] +
      [startTime[i] - endTime[i - 1] for i in range(1, len(startTime))] +
      [eventTime - endTime[-1]]
    )

    ans = 0  # Stores the maximum free time found

    '''
    maxLeft[i] will store the maximum gap from gaps[0] to gaps[i]
    maxRight[i] will store the maximum gap from gaps[i] to gaps[n]
    These help us quickly check if a meeting can be moved elsewhere.
    '''
    maxLeft = [gaps[0]] + [0] * n
    maxRight = [0] * n + [gaps[n]]

    # Fill maxLeft: cumulative max from the left
    for i in range(1, n + 1):
      maxLeft[i] = max(gaps[i], maxLeft[i - 1])

    # Fill maxRight: cumulative max from the right
    for i in range(n - 1, -1, -1):
      maxRight[i] = max(gaps[i], maxRight[i + 1])

    '''
    Try removing each meeting and check:
    - How much total free time is created from adjacent gaps
    - Whether the meeting can be placed somewhere else
    '''
    for i, (start, end) in enumerate(zip(startTime, endTime)):
      currMeetingTime = end - start  # Duration of this meeting

      # Combine gaps before and after the meeting
      adjacentGapsSum = gaps[i] + gaps[i + 1]

      '''
      Check if the meeting can be placed in a non-adjacent gap:
      - Use maxLeft and maxRight to look at all other gaps
      - Exclude the two adjacent ones to avoid overlap
      '''
      canMoveMeeting = currMeetingTime <= max(
          maxLeft[i - 1] if i > 0 else 0,
          maxRight[i + 2] if i + 2 < n + 1 else 0
      )

      '''
      Update answer:
      - Always take the adjacent gaps
      - If meeting can be moved, add back its duration
      '''
      ans = max(ans, adjacentGapsSum +
                (currMeetingTime if canMoveMeeting else 0))

    return ans  # Return the best free time found
