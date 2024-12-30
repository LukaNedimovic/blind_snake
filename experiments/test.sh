#!/bin/bash

cd $SRC_DIR

./simulate_board.py \
    --width 10 \
    --height 10 \
    --strategy "test" \
    --snake_x 9 \
    --snake_y 9 \
    --apple_x 9 \
    --apple_y 5