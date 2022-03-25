import numpy as np


class Board:
    def __init__(self, arr=None, shape=None, periodic=False):
        if arr is not None:
            self._board = arr.astype(bool)
        else:
            self._board   = np.random.randint(0, 2, shape).astype(bool)

        self.periodic = periodic


    def __getitem__(self, indices):
        if isinstance(indices, int):
            indices = (indices,)

        if self.periodic:
            wrapped = tuple([
                indices[i]%self._board.shape[i] for i in range(len(indices))
            ])

            return self._board[wrapped]
        else:
            indices = tuple(indices)

            # Check for out-of-boundsu
            for ind, i in enumerate(indices):
                if (i < 0) or (i >= self._board.shape[ind]):
                    return False

            return self._board[indices]


    def living_neighbor_count(self, i, j):
        return sum((
            self[i-1, j-1],
            self[i-1, j],
            self[i-1, j+1],
            self[i, j-1],
            self[i, j+1],
            self[i+1, j-1],
            self[i+1, j],
            self[i+1, j+1],
        ))


    def add_glider_gun(self, i, j):

        if (self._board.shape[0] < 11) or (self._board.shape[1] < 38):
            raise RuntimeError(
                "Board is too small to add a glider gun. "\
                "Must be at least (11, 38), but is {}".format(self._board.shape)
            )

        gun = np.zeros((11, 38))

        gun[5][1] = gun[5][2] = True
        gun[6][1] = gun[6][2] = True

        gun[3][13] = gun[3][14] = True
        gun[4][12] = gun[4][16] = True
        gun[5][11] = gun[5][17] = True
        gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = True
        gun[7][11] = gun[7][17] = True
        gun[8][12] = gun[8][16] = True
        gun[9][13] = gun[9][14] = True

        gun[1][25] = True
        gun[2][23] = gun[2][25] = True
        gun[3][21] = gun[3][22] = True
        gun[4][21] = gun[4][22] = True
        gun[5][21] = gun[5][22] = True
        gun[6][23] = gun[6][25] = True
        gun[7][25] = True

        gun[3][35] = gun[3][36] = True
        gun[4][35] = gun[4][36] = True

        self._board[i:i+11, j:j+38] = gun


    def update(self):
        new_board = self._board.copy()

        for i in range(self._board.shape[0]):
            for j in range(self._board.shape[1]):
                n = self.living_neighbor_count(i, j)

                if self[i, j]:
                    if (n < 2) or (n > 3):  # Dies from over-/under-crowding
                        new_board[i, j] = False
                else:
                    if n == 3:  # New cell is born
                        new_board[i, j] = True

        # Overwrite old board
        self._board[:] = new_board[:]