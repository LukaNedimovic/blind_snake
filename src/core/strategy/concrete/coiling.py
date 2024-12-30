from core.strategy.strategy import Strategy
from core.strategy.move import Move    
    
class CoilingStrategy(Strategy):
    
    def __init__(self):
        self.directions = [Move.UP, Move.LEFT, Move.DOWN, Move.RIGHT]
        
        self.current_length = 1
        self.current_direction_index = 0
        self.moves_in_current_direction = 0
        self.completed_loops = 0
        
    def sample_move(self, previous_moves: list[Move] = []) -> Move:
        direction = self.directions[self.current_direction_index]

        self.moves_in_current_direction += 1

        if self.moves_in_current_direction == self.current_length:
            self.moves_in_current_direction = 0
            self.current_direction_index = (self.current_direction_index + 1) % len(self.directions)

            if self.current_direction_index == 0:
                self.completed_loops += 1
                self.current_length += 1

        return direction
    
    def reset(self):
        self.current_length = 1
        self.current_direction_index = 0
        self.moves_in_current_direction = 0
        self.completed_loops = 0