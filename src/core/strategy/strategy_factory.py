from core.strategy.concrete.zig_zag import ZigZagStrategy
from core.strategy.concrete.zig_zag_swap import ZigZagSwapStrategy
from core.strategy.concrete.biased_random_walk import BiasedRandomWalkStrategy
from core.strategy.concrete.coiling import CoilingStrategy

class StrategyFactory:
    @classmethod
    def get_strategy(cls, strategy_name):
        match strategy_name:
            case 'zig_zag':
                return ZigZagStrategy()
            case 'zig_zag_swap':
                return ZigZagSwapStrategy()
            case 'biased_random_walk':
                return BiasedRandomWalkStrategy()
            case 'coiling':
                return CoilingStrategy()
            case _:
                raise ValueError(f'Unknown strategy: {strategy_name}')