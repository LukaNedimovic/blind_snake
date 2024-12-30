AVAILABLE_PARSERS = ['simulate_board', 'sweep_boards']

from core.strategy.concrete.zig_zag import ZigZagStrategy
from core.strategy.concrete.zig_zag_swap import ZigZagSwapStrategy
from core.strategy.concrete.biased_random_walk import BiasedRandomWalkStrategy
from core.strategy.concrete.coiling import CoilingStrategy

STRATEGY_MAPPINGS = {
    'zig_zag': ZigZagStrategy,
    'zig_zag_swap': ZigZagSwapStrategy,
    'biased_random_walk': BiasedRandomWalkStrategy,
    'coiling': CoilingStrategy,
}