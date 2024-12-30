#!/usr/bin/env python3

from core.board import Board
from core.engine import Engine
from core.strategy.strategy_factory import StrategyFactory

from utils.argparse import parse_args


def generate_board(args):
    assert (
        (args.snake_x is None and args.snake_y is None) or 
        (args.snake_x is not None and args.snake_y is not None)
    ), 'simulate_board.generate_board() -> Please provide both of snake coordinates'
    
    assert (
        (args.apple_x is None and args.apple_y is None) or 
        (args.apple_x is not None and args.apple_y is not None)
    ), 'simulate_board.generate_board() -> Please provide both of apple coordinates'
    
   
    board = Board(args.width, args.height)
    
    if args.snake_x is not None and args.snake_y is not None:
        assert board.point_within_borders(args.snake_x, args.snake_y), 'simulate_board.generate_board() -> Snake positioned outside the borders.'
    
        board.set_snake_at(args.snake_x, args.snake_y)
    else:
        snake_random_x, snake_random_y = board.random_unoccupied_point()
        board.set_snake_at(snake_random_x, snake_random_y)
        
    
    if args.apple_x is not None and args.apple_y is not None:
        assert board.point_within_borders(args.apple_x, args.apple_y), 'simulate_board.generate_board() -> Apple positioned outside the borders.'

        board.set_apple_at(args.apple_x, args.apple_y)
    else:
        apple_random_x, apple_random_y = board.random_point()
        board.set_apple_at(apple_random_x, apple_random_y)
    
    
    assert board.get_snake() != board.get_apple(), 'simulate_board.generate_board() -> Snake and apple are at the same position.'
    
    return board


if __name__ == '__main__':
    args = parse_args('simulate_board')
    
    board = generate_board(args)
    strategy = StrategyFactory.get_strategy(args.strategy)
    
    engine = Engine(board, strategy)
    engine.simulate()