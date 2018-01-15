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
        self.board = GuiBoard((800, 800))

        self.player = pychess.PieceColor.WHITE

        self.selected = None

    def run(self):
        running = True
        drag = False
        pos = None

        while running:
            dt = self.clock.tick(self.fps_limit)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    drag = True
                    selected = self.board.select_piece(self.board.get_all_pieces(self.player), pygame.mouse.get_pos())

                    if self.selected == selected:
                        self.board.unselect_all()
                        self.selected = None
                    elif not self.selected:
                        self.selected = selected
                        pygame.mouse.set_pos(self.selected.rect.centerx, self.selected.rect.centery)

                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    drag = False

            if self.selected:
                self.selected.update(pos, drag)
                
                if not drag:
                    move = self.selected.valid_destination(pos)

                    if move:
                        self.board.move(move)
                        self.selected.update()
                        
                        self.player = pychess.PieceColor.WHITE if self.player == pychess.PieceColor.BLACK \
                            else pychess.PieceColor.BLACK

                    self.board.unselect_all()
                    self.selected = None

            self.draw()

    def draw(self):
        self.screen.blit(self.board.render(), (0, 0))
        pygame.display.update()


def main():
    chess_game = Chess()

    chess_game.run()

    
if __name__ == "__main__":
    sys.exit(main())
