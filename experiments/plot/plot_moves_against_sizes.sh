#!/bin/bash

"$SRC_DIR/utils/plot.py" \
    --out_path "$EXPERIMENTS_DIR/plot/moves_against_sizes__biased_random_walk__large.png" \
    --file_paths \
        "$EXPERIMENTS_DIR/runs/sweep__biased_random_walk__large.csv" \
        # "$EXPERIMENTS_DIR/runs/sweep__biased_random_walk.csv" \
        # "$EXPERIMENTS_DIR/runs/sweep__zig_zag_swap.csv" \
        # "$EXPERIMENTS_DIR/runs/sweep__zig_zag.csv" \