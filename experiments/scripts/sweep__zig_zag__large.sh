#!/bin/bash

$SRC_DIR/sweep_boards.py \
    --strategy "zig_zag" \
    --min_width 1000 \
    --min_height 1000 \
    --max_width 1000 \
    --max_height 1000 \
    --shots 1 \
    --runs 1000 \
    --out_path "$EXPERIMENTS_DIR/runs/sweep__zig_zag__large.csv"