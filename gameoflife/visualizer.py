class Visualizer:

    def __init__(self, board, method, symbol='o', img=None):
        """
        Args:

            board (:class:`~gol.board.Board`):
                The game board

            method (str):
                One of 'matplotlib' or 'console'

            symbol (str):
                The symbol to use for a live cell if :attr:`method` is 'console'

            img (matplotlib.image.AxesImage, optional):
                The image axis to use for plotting. Only required if
                :attr:`method` is 'matplotlib'

        """

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
        """Displays the board using the provided :attr:`method`"""

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