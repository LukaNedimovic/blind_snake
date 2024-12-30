import csv

def log_outcomes(outcomes: list = [], out_path: str = None):
    if str is None:
        return
    
    header = ['board_width', 'board_height', 'move_count', 'verdict', 'percentage_moves']
    
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        
        for outcome in outcomes:
            percentage_moves = outcome[2] / (35 * outcome[0] * outcome[1])
            writer.writerow([outcome[0], outcome[1], outcome[2], outcome[3], percentage_moves])