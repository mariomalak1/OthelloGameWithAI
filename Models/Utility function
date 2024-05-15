from . import Player, Board, Disk, ComputerPlayer
def evaluate_game_state(board, player):
    opponent = -player

    # Assign weights to each heuristic
    COIN_PARITY_WEIGHT = 1.0
    MOBILITY_WEIGHT = 1.5
    CORNER_WEIGHT = 10.0
    STABILITY_WEIGHT = 3.0

    # Calculate heuristics
    coin_parity_heuristic = calculate_coin_parity_heuristic(board, player)
    mobility_heuristic = calculate_mobility_heuristic(board, player, opponent)
    corner_heuristic = calculate_corner_heuristic(board, player, opponent)
    stability_heuristic = calculate_stability_heuristic(board, player)

    # Calculate the final utility value
    utility_value = (COIN_PARITY_WEIGHT * coin_parity_heuristic +
                     MOBILITY_WEIGHT * mobility_heuristic +
                     CORNER_WEIGHT * corner_heuristic +
                     STABILITY_WEIGHT * stability_heuristic)

    return utility_value


def calculate_coin_parity_heuristic(board, player):
    player_coins = sum(row.count(player) for row in board)
    opponent_coins = sum(row.count(-player) for row in board)
    total_coins = player_coins + opponent_coins

    if total_coins > 0:
        return 100 * (player_coins - opponent_coins) / total_coins
    else:
        return 0


def calculate_mobility_heuristic(board, player, opponent):
    player_moves = len(getPossibleMovesForPlayer(board, player))
    opponent_moves = len(getPossibleMovesForPlayer(board, opponent))
    total_moves = player_moves + opponent_moves

    if total_moves > 0:
        return 100 * (player_moves - opponent_moves) / total_moves
    else:
        return 0


def calculate_corner_heuristic(board, player, opponent):
    player_corners = sum(1 for i, row in enumerate(board) for j, disk in enumerate(row)
                         if (i == 0 or i == 7) and (j == 0 or j == 7) and disk == player)
    opponent_corners = sum(1 for i, row in enumerate(board) for j, disk in enumerate(row)
                           if (i == 0 or i == 7) and (j == 0 or j == 7) and disk == opponent)
    total_corners = player_corners + opponent_corners

    if total_corners > 0:
        return 100 * (player_corners - opponent_corners) / total_corners
    else:
        return 0


def calculate_stability_heuristic(board, player):
    player_stability = calculate_stability(board, player)
    total_positions = 64

    if total_positions > 0:
        return 100 * player_stability / total_positions
    else:
        return 0


def calculate_stability(board, player):
    stability = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == player:
                stability += count_adjacent_opponents(board, player, i, j)
    return stability


def count_adjacent_opponents(board, player, x, y):
    count = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == -player:
            count += 1
    return count
