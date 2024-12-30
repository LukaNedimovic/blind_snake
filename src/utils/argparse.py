import argparse

from utils.const import STRATEGY_MAPPINGS


def non_negative_int(value):
    try:
        ivalue = int(value)
        if ivalue < 0:
            raise argparse.ArgumentTypeError(f'{value} is not a non-negative integer.')

        return ivalue
    
    except ValueError:
        raise argparse.ArgumentTypeError(f'{value} is not an integer.')


def simulate_board_parser():
    parser = argparse.ArgumentParser(description='Blind Snake Game - Single Board Parser')

    parser.add_argument('--width', type=non_negative_int, required=True)
    parser.add_argument('--height', type=non_negative_int, required=True)

    parser.add_argument('--snake_x', type=non_negative_int, required=False)
    parser.add_argument('--snake_y', type=non_negative_int, required=False)
        
    parser.add_argument('--apple_x', type=non_negative_int, required=False)
    parser.add_argument('--apple_y', type=non_negative_int, required=False)


    parser.add_argument('--strategy', type=str, choices=STRATEGY_MAPPINGS.keys(), required=True)


    return parser


def sweep_boards_parser():
    parser = argparse.ArgumentParser(description='Blind Snake Game - Sweep Boards Parser')

    parser.add_argument('--strategy', type=str, choices=STRATEGY_MAPPINGS.keys(), required=True)

    parser.add_argument('--max_width', type=non_negative_int, default=1_000_000, required=False)
    parser.add_argument('--max_height', type=non_negative_int, default=1_000_000, required=False)


    return parser

def get_parser(parser_name: str):
    match parser_name:
        case 'simulate_board':
            return simulate_board_parser()
        case 'sweep_boards':
            return sweep_boards_parser()
        case _:
            raise ValueError('parse_args() -> Invalid parser name.')


def parse_args(parser_name: str):
    parser = get_parser(parser_name)

    args = parser.parse_args()
    return args