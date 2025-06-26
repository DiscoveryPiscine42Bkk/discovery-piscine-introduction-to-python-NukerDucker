#!/usr/bin/env python3
def find_king(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'K':
                return (row, col)
    return None

def is_valid_position(pos, size):
    row, col = pos
    return 0 <= row < size and 0 <= col < size

def check_direction(board, pos, direction, attackers):
    size = len(board)
    row, col = pos
    dr, dc = direction
    row += dr
    col += dc
    while is_valid_position((row, col), size):
        piece = board[row][col]
        if piece != '.':
            return piece in attackers
        row += dr
        col += dc
    return False

def is_under_attack(board, pos):
    size = len(board)
    row, col = pos
    pawn_directions = [(1, -1), (1, 1)]
    for dr, dc in pawn_directions:
        r, c = row + dr, col + dc
        if is_valid_position((r, c), size) and board[r][c] == 'P':
            return True
        
    diagonals = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for direction in diagonals:
        if check_direction(board, pos, direction, {'B', 'Q'}):
            return True
        
    lines = [(-1,0), (1,0), (0,-1), (0,1)]
    for direction in lines:
        if check_direction(board, pos, direction, {'R', 'Q'}):
            return True
            
    return False

def checkmate(board_str):
    try:
        board = [list(row) for row in board_str.strip().split('\n')]
        king_pos = find_king(board)
        
        if not king_pos:
            return "Fail (No King Found)"
        if not is_under_attack(board, king_pos):
            return "Fail (King not under attack)"

        return "Success"
    except Exception as e:
        return "Error"