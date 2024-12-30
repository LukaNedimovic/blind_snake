import random
from enum import Enum

from core.strategy.strategy import Strategy
from core.strategy.move import Move


class Direction(Enum):
    DOWN_RIGHT = 0
    DOWN_LEFT = 1
    
    
class ZigZagSwapStrategy(Strategy):
    def __init__(self):
        self.direction = Direction.DOWN_RIGHT
        pass
    
    def sample_move(self, previous_moves: list[Move] = []) -> Move:
        swap_chance = random.random()
        if swap_chance < 0.05:
            self.direction = Direction.DOWN_RIGHT if self.direction == Direction.DOWN_LEFT else Direction.DOWN_LEFT
        
        
        if Direction.DOWN_RIGHT:
            if previous_moves == []:
                return Move.RIGHT
            
            last_move = previous_moves[-1]
            return Move.DOWN if (last_move == Move.RIGHT or last_move == Move.LEFT) else Move.RIGHT
        
        else:
            if previous_moves == []:
                return Move.LEFT
            
            last_move = previous_moves[-1]
            return Move.DOWN if (last_move == Move.LEFT or last_move == Move.RIGHT) else Move.LEFT 
        
    def reset(self):
        self.direction = Direction.DOWN_RIGHT           