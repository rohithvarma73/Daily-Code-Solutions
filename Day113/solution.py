from dataclasses import dataclass
import collections, bisect   # Required imports

# Define an immutable packet with source, destination, and timestamp
@dataclass(frozen=True)
class Packet:
  source: int
  destination: int
  timestamp: int


class Router:
  def __init__(self, memoryLimit: int):
    self.memoryLimit = memoryLimit  # Maximum packets the router can hold
    self.uniquePackets: set[Packet] = set()  # Track unique packets
    self.packetQueue: collections.deque[Packet] = collections.deque()  # FIFO queue for packets
    self.destinationTimestamps = collections.defaultdict(list)  # Store timestamps per destination
    self.processedPacketIndex = collections.Counter()  # Count packets processed per destination

  def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
    packet = Packet(source, destination, timestamp)  # Create a packet
    if packet in self.uniquePackets:  # Reject if duplicate
      return False
    if len(self.packetQueue) == self.memoryLimit:  # If full, forward (remove) one packet
      self.forwardPacket()
    self.packetQueue.append(packet)  # Add packet to queue
    self.uniquePackets.add(packet)  # Mark packet as unique
    if destination not in self.destinationTimestamps:  # Ensure destination list exists
      self.destinationTimestamps[destination] = []
    self.destinationTimestamps[destination].append(timestamp)  # Save timestamp for lookup
    return True  # Packet successfully added

  def forwardPacket(self) -> list[int]:
    if not self.packetQueue:  # No packet to forward
      return []
    nextPacket = self.packetQueue.popleft()  # Remove the oldest packet
    self.uniquePackets.remove(nextPacket)  # Free memory from unique set
    self.processedPacketIndex[nextPacket.destination] += 1  # Mark one more processed for this destination
    return [nextPacket.source, nextPacket.destination, nextPacket.timestamp]  # Return forwarded packet info

  def getCount(self, destination: int, startTime: int, endTime: int) -> int:
    if destination not in self.destinationTimestamps:  # No packets for destination
      return 0
    timestamps = self.destinationTimestamps[destination]  # Get timestamps for destination
    startIndex = self.processedPacketIndex.get(destination, 0)  # Skip already processed packets
    lowerBound = bisect.bisect_left(timestamps, startTime, startIndex)  # First timestamp >= startTime
    upperBound = bisect.bisect_right(timestamps, endTime, startIndex)  # First timestamp > endTime
    return upperBound - lowerBound  # Count of packets in the given time range
