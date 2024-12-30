#!/bin/bash

$SRC_DIR/sweep_boards.py \
    --strategy "coiling" \
    --min_width 1000 \
    --min_height 1000 \
    --max_width 1000 \
    --max_height 1000 \
    --shots 1 \
    --runs 1000 \
    --out_path "$EXPERIMENTS_DIR/runs/sweep__coiling__large.csv"