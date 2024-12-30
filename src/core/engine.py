from core.board import Board
from core.strategy.strategy import Strategy

import random

from utils.log import log_outcomes
from tqdm import tqdm

class Engine:
    def __init__(self, board: Board = None, strategy: Strategy = None):
        self.board = board
        self.strategy = strategy

    def load_board(self, board: Board):
        self.board = board

    def load_strategy(self, strategy: Strategy):
        self.strategy = strategy
        
    def simulate(self, log: bool = False):
        assert (self.board is not None), 'Engine.simulate() -> Board not set.'
        assert (self.strategy is not None), 'Engine.simulate() -> Strategy not set.'
        
        if self.board.width * self.board.height > 1_000_000:
            return None
        
        if log:
            print("Initial board:")
            self.board.draw()
            print()
            print()
            
        upper_limit = 35 * self.board.width * self.board.height
        
        move_count = 0
        previous_moves = []
        while (move_count < upper_limit) and (not self.board.is_snake_at(self.board.get_apple())):
            move = self.strategy.sample_move(previous_moves)
            self.board.send_move(move)
            
            previous_moves.append(move)
            move_count += 1
            
            if log:
                self.board.draw()
                print()
            
        if log:
            print(f'Board({self.board.width} x {self.board.height}) [{self.strategy.__class__.__name__}]: {move_count} moves, {"success" if self.board.is_snake_at(self.board.get_apple()) else "failure"}')
        
        return self.board.width, self.board.height, move_count, self.board.is_snake_at(self.board.get_apple())
    
    def sweep_boards(
        self, 
        min_width: int = 1,
        min_height: int = 1, 
        max_width: int = 1_000_000, 
        max_height: int = 1_000_000, 
        runs: int = -1,
        shots: int = 128, 
        out_path: str = None, 
        log: bool = False
    ):
        outcomes = []
        
        if runs != -1:
            print(f'Runnning sweep_boards with {runs} runs')
            progress_bar = tqdm(total=runs, desc=f'Sweeping {runs} boards')

            boards = self.generate_n_boards(runs, min_width, min_height, max_width, max_height)
            for board in boards:
                self.load_board(board)
                
                outcome = self.simulate(log=log)
                outcomes.append(outcome)
                
                self.board = None
                del board
                
                self.strategy.reset()
                progress_bar.update(1)
                
            progress_bar.close()
            
        else:        
            total_shots = min(shots, max_width - 1) * (max_width - 1) + min(shots, max_height - 1) * (max_height - 1) + min(shots, max_width * max_height) * (max_width - 1) * (max_height - 1)
            progress_bar = tqdm(total=total_shots, desc='Sweeping boards')

            shots = min(shots, max_width - min_width)
            for shot in range(shots):
                for width in range(2, max_width + 1):
                    board = Board(width, 1)
                    board.generate_random_board()
                    self.load_board(board)
                    
                    outcome = self.simulate(log=log)
                    outcomes.append(outcome)
                    
                    self.board = None
                    del board
                    
                    self.strategy.reset()
                    progress_bar.update(1)
            
            shots = min(shots, max_height - min_height)            
            for shot in range(shots):
                for height in range(2, max_height + 1):
                    board = Board(1, height)
                    board.generate_random_board()
                    self.load_board(board)
                    
                    outcome = self.simulate(log=log)
                    outcomes.append(outcome)
                    
                    self.board = None
                    del board
                    
                    self.strategy.reset()
                    progress_bar.update(1)

            shots = min(shots, max_width * max_height)
            for shot in range(shots):
                for width in range(2, max_width + 1):
                    for height in range(2, max_height + 1):
                        board = Board(width, height)
                        board.generate_random_board()
                        self.load_board(board)
                        
                        outcome = self.simulate(log=log)
                        outcomes.append(outcome)
                        
                        self.board = None
                        del board
                        
                        self.strategy.reset()
                        progress_bar.update(1)

            progress_bar.close()
                    
        self.analyze_outcomes(outcomes)
        log_outcomes(outcomes, out_path)
        
    def analyze_outcomes(self, outcomes: list):
        # 0 - width
        # 1 - height
        # 2 - move count
        # 3 - verdict
        print(f'Number of simulations: {len(outcomes)}')
        print(f'Number of successful simulations: {len([outcome for outcome in outcomes if outcome[3]])}')
        print(f'Number of failed simulations: {len([outcome for outcome in outcomes if not outcome[3]])}')
        print(f'Succes rate: {len([outcome for outcome in outcomes if outcome[3]]) / len(outcomes) * 100:.2f}%')
        
    def generate_n_boards(self, runs, min_width, min_height, max_width, max_height):
        boards = []
        for run in range(runs):
            width = random.randint(min_width, max_width)
            height = random.randint(min_height, max_height)
            
            board = Board(width, height)
            board.generate_random_board()
            
            boards.append(board)
        
        return boards