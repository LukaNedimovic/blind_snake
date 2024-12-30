#!/bin/bash

$SRC_DIR/sweep_boards.py \
    --strategy "biased_random_walk" \
    --max_width 100 \
    --max_height 100 \
    --shots 16 \
    --out_path "$EXPERIMENTS_DIR/runs/sweep__biased_random_walk.csv"