class Visualizer:

    def __init__(self, board, method, symbol='o', img=None):
        self.board  = board
        self.method = method
        self.s      = symbol
        self.img    = img

        if self.method == 'splines':
            if self.img is None:
                raise RuntimeError(
                    "Must provide plotting axis if using method=='matplotlib'"
                )

        self.frame = 0


    def show(self):

        if self.method == 'console':
            n, m = self.board._board.shape

            print(f"Frame: {self.frame}")
            print('', '-'*m)
            for i in range(n):
                print('|', end='')
                for j in range(m):
                    print(self.s if self.board[i,j] else ' ', end='')
                print('|')
            print('', '-'*m)
        else:
            self.img.set_data(self.board)

        self.frame += 1