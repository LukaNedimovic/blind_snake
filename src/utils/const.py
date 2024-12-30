AVAILABLE_PARSERS = ['simulate_board', 'sweep_boards']

from core.strategy.concrete.zig_zag import ZigZagStrategy
from core.strategy.concrete.zig_zag_swap import ZigZagSwapStrategy
from core.strategy.concrete.biased_random_walk import BiasedRandomWalkStrategy

STRATEGY_MAPPINGS = {
    'zig_zag': ZigZagStrategy,
    'zig_zag_swap': ZigZagStrategy,
    'biased_random_walk': BiasedRandomWalkStrategy,
}