#!/usr/bin/env python3

import pandas as pd
import sys

def count_successes_and_fails(file_path):
    df = pd.read_csv(file_path)
    
    success_count = df['verdict'].sum()
    fail_count = len(df) - success_count
    success_rate = (success_count / len(df)) * 100
    
    print(f'Successes: {success_count} | Fails: {fail_count} | Success Rate: {success_rate:.2f}%')
    
    return success_count, fail_count, success_rate


if __name__ == '__main__':
    count_successes_and_fails(sys.argv[1])