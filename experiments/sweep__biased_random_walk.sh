#!/bin/bash

cd $SRC_DIR

./sweep_boards.py \
    --strategy "biased_random_walk" \
    --max_width 50 \
    --max_height 50 \