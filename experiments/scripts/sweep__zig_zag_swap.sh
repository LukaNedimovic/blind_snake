#!/bin/bash

$SRC_DIR/sweep_boards.py \
    --strategy "zig_zag_swap" \
    --max_width 100 \
    --max_height 100 \
    --shots 16 \
    --out_path "$EXPERIMENTS_DIR/runs/sweep__zig_zag_swap.csv"