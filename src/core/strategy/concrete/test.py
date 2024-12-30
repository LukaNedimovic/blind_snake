from core.board import Board
from core.strategy.strategy import Strategy
from core.strategy.move import Move

class Test(Strategy):
    def sample_move(self):
        return Move.UP