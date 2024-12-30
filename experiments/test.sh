#!/bin/bash

cd $SRC_DIR

./simulate_board.py \
    --width 6 \
    --height 6 \
    --strategy "coiling" \