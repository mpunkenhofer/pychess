import sys
import pychess
import pygame


class GraphicalChess:
    def __init__(self, variant):
        self.variant = variant


def main():
    chess_game = GraphicalChess(pychess.variant.Standard)

    
if __name__ == "__main__":
    sys.exit(main())
