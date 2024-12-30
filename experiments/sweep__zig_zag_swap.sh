#!/bin/bash

cd $SRC_DIR

./sweep_boards.py \
    --strategy "zig_zag_swap" \
    --max_width 24 \
    --max_height 24 \