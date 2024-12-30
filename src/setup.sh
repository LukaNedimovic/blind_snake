#!/bin/bash

if ! conda env list | grep -q "blind_snake_env"; then
    conda env create -f requirements.txt -n blind_snake_env
fi

source activate blind_snake_env

SRC_DIR=$(pwd)
EXPERIMENTS_DIR="$SRC_DIR/../experiments"

export PYTHONPATH=$SRC_DIR

export SRC_DIR
export EXPERIMENTS_DIR