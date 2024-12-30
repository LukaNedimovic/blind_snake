#!/bin/bash

cd $SRC_DIR

./sweep_boards.py \
    --strategy "coiling" \
    --max_width 50 \
    --max_height 50 \