# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import sys
import pychess
import pygame

from examples.guichess import GuiBoard


class Chess:
    def __init__(self, variant, size=(1054, 1054), fps_limit=60):
        self.variant = variant
        self.fps_limit = fps_limit

        pygame.init()
        self.screen = pygame.display.set_mode(size)

        # init the clock
        self.clock = pygame.time.Clock()

        # init the board
        self.board = GuiBoard(pygame.Surface((1054, 1054)))

    def run(self):
        running = True

        while running:
            dt = self.clock.tick(self.fps_limit)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.draw()

    def draw(self):
        self.screen.blit(self.board.render(), (0, 0))
        pygame.display.update()


def main():
    chess_game = Chess(pychess.variant.Standard())

    chess_game.run()

    
if __name__ == "__main__":
    sys.exit(main())
