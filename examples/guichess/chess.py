# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import sys
import pygame
import pychess

from examples.guichess import GuiBoard


class Chess:
    def __init__(self, size=(800, 800), fps_limit=60):
        self.fps_limit = fps_limit

        pygame.init()
        self.screen = pygame.display.set_mode(size)

        # init the clock
        self.clock = pygame.time.Clock()
        # init the board
        self.board = GuiBoard(self, (800, 800))

        self.player = pychess.PieceColor.WHITE

        self.selected = None

    def run(self):
        running = True

        while running:
            dt = self.clock.tick(self.fps_limit)
            running = self.handle_events()

            self.draw()

    def next_player(self):
        self.player = pychess.PieceColor.BLACK if self.player == pychess.PieceColor.WHITE else pychess.PieceColor.WHITE

    def draw(self):
        self.screen.blit(self.board.render(), (0, 0))
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            else:
                self.board.handle_event(event, self.player)

        return True


def main():
    chess_game = Chess()

    chess_game.run()

    
if __name__ == "__main__":
    sys.exit(main())
