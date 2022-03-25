import unittest
import numpy as np

from gameoflife.board import Board


class TestBoard(unittest.TestCase):


    def test_constructor(self):
        arr = np.random.randint(0, 2, (3, 3))
        board = Board(arr, periodic=False)

        assert arr[0, 0] == board[0, 0]

    def test_nonperiodic_oob(self):
        arr = np.random.randint(0, 2, (3, 3))
        board = Board(arr, periodic=False)

        assert not board[3, 3]


    def test_periodicity(self):
        arr = np.random.randint(0, 2, (3, 3))
        board = Board(arr, periodic=True)

        assert arr[0, 0] == board[0, 3]
        assert arr[0, 0] == board[3, 0]
        assert arr[0, 0] == board[3, 3]

        assert arr[0, 2] == board[0,  -1]
        assert arr[2, 0] == board[-1,  0]
        assert arr[2, 2] == board[-1, -1]

    
    def test_basic_neighbor_count(self):
        board = Board(
            np.array([
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
            ]),
            periodic=False
        )

        assert board.living_neighbor_count(0, 0) == 1
        assert board.living_neighbor_count(0, 1) == 1
        assert board.living_neighbor_count(0, 2) == 1
        assert board.living_neighbor_count(1, 0) == 1
        assert board.living_neighbor_count(1, 1) == 0
        assert board.living_neighbor_count(1, 2) == 1
        assert board.living_neighbor_count(2, 0) == 1
        assert board.living_neighbor_count(2, 1) == 1
        assert board.living_neighbor_count(2, 2) == 1


    def test_basic_neighbor_count_periodic(self):
        board = Board(
            np.array([
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
            ]),
            periodic=True
        )

        assert board.living_neighbor_count(0, 0) == 1
        assert board.living_neighbor_count(0, 1) == 1
        assert board.living_neighbor_count(0, 2) == 1
        assert board.living_neighbor_count(1, 0) == 1
        assert board.living_neighbor_count(1, 1) == 0
        assert board.living_neighbor_count(1, 2) == 1
        assert board.living_neighbor_count(2, 0) == 1
        assert board.living_neighbor_count(2, 1) == 1
        assert board.living_neighbor_count(2, 2) == 1


    def test_basic_neighbor_count_multiple(self):
        board = Board(
            np.array([
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0],
            ]),
            periodic=False
        )

        assert board.living_neighbor_count(0, 0) == 3
        assert board.living_neighbor_count(0, 1) == 3
        assert board.living_neighbor_count(0, 2) == 3
        assert board.living_neighbor_count(1, 0) == 3
        assert board.living_neighbor_count(1, 1) == 4
        assert board.living_neighbor_count(1, 2) == 3
        assert board.living_neighbor_count(2, 0) == 3
        assert board.living_neighbor_count(2, 1) == 3
        assert board.living_neighbor_count(2, 2) == 3


    def test_tricky_neighbor_count_periodic(self):
        board = Board(
            np.array([
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
            ]),
            periodic=True
        )

        assert board.living_neighbor_count(0, 0) == 1
        assert board.living_neighbor_count(0, 1) == 0
        assert board.living_neighbor_count(0, 2) == 0
        assert board.living_neighbor_count(0, 3) == 1
        assert board.living_neighbor_count(0, 4) == 1

        assert board.living_neighbor_count(1, 0) == 0
        assert board.living_neighbor_count(1, 1) == 1
        assert board.living_neighbor_count(1, 2) == 1
        assert board.living_neighbor_count(1, 3) == 1
        assert board.living_neighbor_count(1, 4) == 0

        assert board.living_neighbor_count(2, 0) == 0
        assert board.living_neighbor_count(2, 1) == 1
        assert board.living_neighbor_count(2, 2) == 0
        assert board.living_neighbor_count(2, 3) == 1
        assert board.living_neighbor_count(2, 4) == 0

        assert board.living_neighbor_count(3, 0) == 1
        assert board.living_neighbor_count(3, 1) == 1
        assert board.living_neighbor_count(3, 2) == 1
        assert board.living_neighbor_count(3, 3) == 2
        assert board.living_neighbor_count(3, 4) == 1

        assert board.living_neighbor_count(4, 0) == 1
        assert board.living_neighbor_count(4, 1) == 0
        assert board.living_neighbor_count(4, 2) == 0
        assert board.living_neighbor_count(4, 3) == 1
        assert board.living_neighbor_count(4, 4) == 0


    def test_growth(self):
        board = Board(
            np.array([
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]),
            periodic=True
        )

        board.update()

        assert board[1, 1]