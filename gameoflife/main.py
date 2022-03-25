import os
import time
import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from gameoflife.board import Board
from gameoflife.visualizer import Visualizer

parser = argparse.ArgumentParser(
    description="Runs Conway's Game of Life simulation."
)

# Add arguments
parser.add_argument(
    '--grid-size',
    type=int,
    help='The side length to use for a square board',
    dest='grid_size',
    default=50,
    required=True,
)

parser.add_argument(
    '--periodic',
    type=bool,
    help='If True, uses periodic boundary conditions for the board',
    dest='periodic',
    default=True,
    required=True
)

parser.add_argument(
    '--output-method',
    type=str,
    help='Output method. One of "console" or "matplotlib"',
    dest='output',
    default='console',
    required=False
)


parser.add_argument(
    '--mov-file',
    type=str,
    help='File name for saving video if output method is "matplotlib"',
    dest='movfile',
    required=False
)

parser.add_argument(
    '--duration',
    type=int,
    help='Number of times to update the game',
    dest='duration',
    default=100,
    required=False
)

parser.add_argument(
    '--interval',
    type=int,
    help='Animation update interval',
    dest='interval',
    default=1,
    required=False
)

parser.add_argument(
    '--symbol',
    type=str,
    help='The symbol to use for a cell in console output',
    dest='symbol',
    default='o',
    required=False,
)


parser.add_argument(
    '--glider',
    type=bool,
    help='If True, builds a Gosper glider gun at index (0, 0)',
    dest='glider',
    default=False,
    required=False,
)

args = parser.parse_args()


def main():
    board = Board(
        shape=(args.grid_size, args.grid_size),
        periodic=args.periodic
    )

    if args.glider:
        board._board[:] = False
        board.add_glider_gun(0, 0)

    if args.output == 'matplotlib':
        fig, ax = plt.subplots()

        img = ax.imshow(board._board)

    else:
        img = None

    visualizer = Visualizer(
        board=board,
        method=args.output,
        symbol=args.symbol,
        img=img,
    )

    clear = lambda: os.system('clear')
    # clear = lambda: print()

    def step():
        board.update()
        clear()
        visualizer.show()
        # time.sleep(0.05)

    if args.output == 'matplotlib':
        ani = animation.FuncAnimation(
            fig,
            step,
            frames=args.duration,
            interval=args.interval,
        )

        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
    else:

        clear()
        visualizer.show()

        for _ in range(args.duration):
            step()


if __name__ == '__main__':
    main()
