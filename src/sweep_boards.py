#!/usr/bin/env python3

from core.engine import Engine
from core.strategy.strategy_factory import StrategyFactory
from utils.argparse import parse_args

if __name__ == '__main__':
    args = parse_args('sweep_boards')
    
    strategy = StrategyFactory.get_strategy(args.strategy)
    
    engine = Engine(strategy=strategy)
    engine.sweep_boards(max_width=args.max_width, max_height=args.max_height)