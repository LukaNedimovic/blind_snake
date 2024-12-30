#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import itertools

from argparser import parse_args

def plot_results(file_paths: list, out_path: str):
    colors = itertools.cycle(plt.cm.tab10.colors)
    markers = itertools.cycle(('o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X'))
    
    for file_path in file_paths:
        data = pd.read_csv(file_path)
        
        board_size = data['board_width'] * data['board_height']
        
        label = file_path.split('/')[-1].split('.')[0]
        marker = next(markers)
        if marker == 'o':
            plt.scatter(board_size, data['percentage_moves'], label=label, edgecolor=next(colors), facecolor='none', marker=marker, s=10)
        else:
            plt.scatter(board_size, data['percentage_moves'], label=label, color=next(colors), marker=marker, s=10)

    plt.xlabel('Board Size')
    plt.ylabel('Percentage of Moves')
    plt.title('Percentage of Moves vs Board Size')
    plt.legend()
    
    plt.savefig(out_path)


if __name__ == '__main__':
    args = parse_args('plot')
    
    plot_results(args.file_paths, args.out_path)