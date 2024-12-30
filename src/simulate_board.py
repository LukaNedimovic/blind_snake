#!/usr/bin/env python3

import argparse

from core.board import Board
from core.engine import Engine

from core.strategy import strategy
from core.strategy.concrete.test import Test

AVAILABLE_STRATEGIES = ['test']
STRATEGY_MAPPING = {'test': Test}


def non_negative_int(value):
    try:
        ivalue = int(value)
        if ivalue < 0:
            raise argparse.ArgumentTypeError(f'{value} is not a non-negative integer.')

        return ivalue
    
    except ValueError:
        raise argparse.ArgumentTypeError(f'{value} is not an integer.')


def parse_args():
    parser = argparse.ArgumentParser(description='Blind Snake Game - Single Board Parser')

    parser.add_argument('--width', type=non_negative_int, required=True)
    parser.add_argument('--height', type=non_negative_int, required=True)

    parser.add_argument('--snake_x', type=non_negative_int, required=False)
    parser.add_argument('--snake_y', type=non_negative_int, required=False)
        
    parser.add_argument('--apple_x', type=non_negative_int, required=False)
    parser.add_argument('--apple_y', type=non_negative_int, required=False)

    parser.add_argument('--strategy', type=str, choices=AVAILABLE_STRATEGIES, required=True)


    args = parser.parse_args()
    print('Arguments parsed')
    return args


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
    
    print('Board generated')
    return board

def get_strategy(strategy_name: str):
    Strategy_selected = STRATEGY_MAPPING.get(strategy_name)
    
    return Strategy_selected()  # Create a strategy instance

if __name__ == '__main__':
    print('Start')
    args = parse_args()
    
    board = generate_board(args)
    strategy = get_strategy(args.strategy)
    engine = Engine(board, strategy)
    
    # board.draw()
    
    print(engine.simulate())