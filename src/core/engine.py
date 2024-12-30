from core.board import Board
from core.strategy.strategy import Strategy

class Engine:
    def __init__(self):
        pass
    
    def __init__(self, board: Board, strategy: Strategy):
        self.board = board
        self.strategy = strategy

    def load_board(self, board: Board):
        self.board = board

    def load_strategy(self, strategy: Strategy):
        self.strategy = strategy
        
    def simulate(self):
        assert (self.board is not None), 'Engine.simulate() -> Board not set.'
        assert (self.strategy is not None), 'Engine.simulate() -> Strategy not set.'
        
        upper_limit = 1 * self.board.width * self.board.height
        
        move_count = 0
        while (move_count < upper_limit) and (not self.board.is_snake_at(self.board.get_apple())):
            move = self.strategy.sample_move()
            self.board.send_move(move)
            
            move_count += 1
            
            self.board.draw()
            print()
        
        return move_count, self.board.is_snake_at(self.board.get_apple())