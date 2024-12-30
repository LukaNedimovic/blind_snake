from core.board import Board
from core.strategy.strategy import Strategy

class Engine:
    def __init__(self, board: Board = None, strategy: Strategy = None):
        self.board = board
        self.strategy = strategy

    def load_board(self, board: Board):
        self.board = board

    def load_strategy(self, strategy: Strategy):
        self.strategy = strategy
        
    def simulate(self):
        assert (self.board is not None), 'Engine.simulate() -> Board not set.'
        assert (self.strategy is not None), 'Engine.simulate() -> Strategy not set.'
        
        if self.board.width * self.board.height > 1_000_000:
            return
        
        # print("Initial board:")
        # self.board.draw()
        # print()
        # print()
        
        upper_limit = 35 * self.board.width * self.board.height
        
        move_count = 0
        previous_moves = []
        while (move_count < upper_limit) and (not self.board.is_snake_at(self.board.get_apple())):
            move = self.strategy.sample_move(previous_moves)
            self.board.send_move(move)
            
            previous_moves.append(move)
            move_count += 1
            
            # self.board.draw()
            # print()
        
        
        print(f'Board({self.board.width} x {self.board.height}) [{self.strategy.__class__.__name__}]: {move_count} moves, {"success" if self.board.is_snake_at(self.board.get_apple()) else "failure"}')
        return move_count, self.board.is_snake_at(self.board.get_apple())
    
    def sweep_boards(self, shots = 128, max_width: int = 1_000_000, max_height: int = 1_000_000):
        outcomes = []
        
        shots = min(shots, max_width - 1)
        for shot in range(shots):
            for width in range(2, max_width + 1):
                board = Board(width, 1)
                board.generate_random_board()
                self.load_board(board)
                
                outcome = self.simulate()
                outcomes.append(outcome)
                
                self.board = None
                del board
                
                self.strategy.reset()
        
        shots = min(shots, max_height - 1)            
        for shot in range(shots):
            for height in range(2, max_height + 1):
                board = Board(1, height)
                board.generate_random_board()
                self.load_board(board)
                
                outcome = self.simulate()
                outcomes.append(outcome)
                
                self.board = None
                del board
                
                self.strategy.reset()

        shots = min(shots, max_width * max_height)
        for shot in range(shots):
            for width in range(2, max_width + 1):
                for height in range(2, max_height + 1):
                    board = Board(width, height)
                    board.generate_random_board()
                    self.load_board(board)
                    
                    outcome = self.simulate()
                    outcomes.append(outcome)
                    
                    self.board = None
                    del board
                    
                    self.strategy.reset()
                    
        self.analyze_outcomes(outcomes)
        
    def analyze_outcomes(self, outcomes: list):
        print(f'Number of simulations: {len(outcomes)}')
        print(f'Number of successful simulations: {len([outcome for outcome in outcomes if outcome[1]])}')
        print(f'Number of failed simulations: {len([outcome for outcome in outcomes if not outcome[1]])}')
        print(f'Succes rate: {len([outcome for outcome in outcomes if outcome[1]]) / len(outcomes) * 100:.2f}%')