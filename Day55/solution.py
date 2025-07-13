from typing import List  # Import List from typing module for type hints

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort the list of players in ascending order
        players.sort()
        # Sort the list of trainers in ascending order
        trainers.sort()
      
        # Initialize the count of matched players and trainers
        match_count = 0
        # Initialize the pointer for trainers list
        trainer_index = 0
      
        # Iterate over each player in the sorted list
        for player in players:
            # Skip trainers which have less capacity than the current player's strength
            while trainer_index < len(trainers) and trainers[trainer_index] < player:
                trainer_index += 1
              
            # If there is a trainer that can match the current player
            if trainer_index < len(trainers):
                # Increment the match count
                match_count += 1
                # Move to the next trainer for the next player
                trainer_index += 1
      
        # Return the total number of matches
        return match_count
