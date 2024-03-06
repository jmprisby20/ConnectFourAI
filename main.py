from pack.Board import Board

# Main Method
if __name__ == '__main__':
    player_turn = 0 # Stores player number whose turn it is
    is_game_over = False # Flag for main loop

    b = Board()
    while not is_game_over:
        b.print_board()
        b.player_turn(player_turn)
        if b.check_win(player_turn):
            is_game_over = True
            b.print_board()
            print(f"Player {player_turn + 1} Wins!!!")
        else:
            if player_turn == 0:
                player_turn = 1
            else: 
                player_turn = 0