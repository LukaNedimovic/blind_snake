#!/bin/bash

$SRC_DIR/sweep_boards.py \
    --strategy "biased_random_walk" \
    --min_width 1000 \
    --min_height 1000 \
    --max_width 1000 \
    --max_height 1000 \
    --shots 1 \
    --runs 100 \
    --out_path "$EXPERIMENTS_DIR/runs/sweep__biased_random_walk__large.csv"