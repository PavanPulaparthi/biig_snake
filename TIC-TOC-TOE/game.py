class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we use a single list of rep 3x3 board
        self.current_winner = None # keep track of winner!

    def print_board(self):
        # this is just getting rows
        for row in [self.board [i*3:(i+1)*3] for i in range(3)]:
            print ('|' + '|'.join(row) + ' |')
    
    @staticmethod
    