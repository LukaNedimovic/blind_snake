#!/usr/bin/env python3

from core.engine import Engine
from core.strategy.strategy_factory import StrategyFactory
from utils.argparser import parse_args

if __name__ == '__main__':
    args = parse_args('sweep_boards')
    
    strategy = StrategyFactory.get_strategy(args.strategy)
    
    engine = Engine(strategy=strategy)
    engine.sweep_boards(
        min_width=args.min_width,
        min_height=args.min_height,
        max_width=args.max_width, 
        max_height=args.max_height,
        runs=args.runs,
        shots=args.shots, 
        out_path=args.out_path,
        log=args.log,
    )