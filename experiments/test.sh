#!/bin/bash

cd $SRC_DIR

./simulate_board.py \
    --width 10 \
    --height 10 \
    --strategy "zig_zag" \