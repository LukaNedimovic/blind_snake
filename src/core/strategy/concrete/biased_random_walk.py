import random

from core.strategy.strategy import Strategy
from core.strategy.move import Move    
    
class BiasedRandomWalkStrategy(Strategy):
    def sample_move(self, previous_moves: list[Move] = []) -> Move:
        moves = [Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT]
        if previous_moves == []:
            return random.choice(moves)
        
        last_move = previous_moves[-1] if previous_moves else None
        bias = 0.5
        leftover = (1 - bias) / 3
        weights = [bias if i != last_move.value else leftover for i in range(4)]
        
        return random.choices(moves, weights=weights, k=1)[0]