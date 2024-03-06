class Board:

    def __init__(self):
        # Init an empty board
        self.Board = [ 
            [ -1, -1, -1, -1, -1, -1, -1],
            [ -1, -1, -1, -1, -1, -1, -1],
            [ -1, -1, -1, -1, -1, -1, -1],
            [ -1, -1, -1, -1, -1, -1, -1],
            [ -1, -1, -1, -1, -1, -1, -1],
            [ -1, -1, -1, -1, -1, -1, -1]
        ]


    # Desc.: Checks if a given player has won the game with current board
    # Input: player_num - player who we are checking
    # Output: True/False 
    # NOTE: Since the game is turn based we can just check for the player who made the last turn since you cannot lose on 
    #       your own turn.
    def check_win(self, player_num):
        # Check if a given play has won the game
        # Go from bottom row up
        for r in range(6): 
            # Check for each column
            for c in range(7):
                # Check for horizontal win
                if ( c <= 3 ):
                    if ( 
                        self.Board[r][c] == player_num and
                        self.Board[r][c + 1] == player_num and
                        self.Board[r][c + 2] == player_num and 
                        self.Board[r][c + 3] == player_num
                    ):
                        # Here this is a horizontal win
                        return True

                # Check for vertical win
                if ( r <= 2 ):
                    if (
                        self.Board[r][c] == player_num and
                        self.Board[r + 1][c] == player_num and
                        self.Board[r + 2][c] == player_num and
                        self.Board[r + 3][c] == player_num
                    ):
                        # Here this is vertical win
                        return True
                
                # Check for diagonal wins
                # Downward diagonal
                if r <= 2 and c <= 3:
                    if (
                        self.Board[r][c] == player_num and
                        self.Board[r+1][c+1] == player_num and
                        self.Board[r+2][c+2] == player_num and
                        self.Board[r+3][c+3] == player_num
                    ):
                        return True
                # Upward diagonal
                if r >= 3 and c <= 3:
                    if (
                        self.Board[r][c] == player_num and
                        self.Board[r-1][c+1] == player_num and
                        self.Board[r-2][c+2] == player_num and
                        self.Board[r-3][c+3] == player_num
                    ):
                        return True
        return False

    # Desc.: Prints board to console
    def print_board(self):
        str = ''
        board_symbols = {-1: ' ', 0: 'O', 1: 'X'}
        for r in range(6):
            s = ''
            for c in range(7):
                s += f"| {board_symbols[self.Board[r][c]]} "
                if c == 6:
                    s += '|\n'
            str += s
        str += '  1   2   3   4   5   6   7   '
        print(str)

    # Desc.: Gets the row number of the first available row in a given column
    def col_get_first_avail(self, col_number):
        for r in reversed(range(6)):
            if (self.Board[r][col_number] == -1):
                return r
        return -1

    def player_turn(self, player_num):
        turn_success = False
        while not turn_success:
            try:
                print(f"Player {player_num + 1}, Enter column number to play: ")
                i = int(input())
                if ( i > 0 and i < 8):
                    row_inserted = self.col_get_first_avail(i-1)
                    if ( row_inserted != - 1):
                        self.Board[row_inserted][i-1] = player_num
                        turn_success = True
                    else:
                        print('Error: Column Full')
            except Exception as e:
                print("Error: Enter Value in range of 1-7")