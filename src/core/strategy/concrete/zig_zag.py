from core.strategy.strategy import Strategy
from core.strategy.move import Move


class ZigZagStrategy(Strategy):
    def sample_move(self, previous_moves: list[Move] = []) -> Move:
        if previous_moves == []:
            return Move.RIGHT
        
        last_move = previous_moves[-1]
        return Move.DOWN if last_move == Move.RIGHT else Move.RIGHT