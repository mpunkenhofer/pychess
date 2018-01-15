# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import pychess
import pygame

from examples.guichess.resources import SpriteSheetPositions, SpriteSize


class GuiPiece(pygame.sprite.Sprite):
    def __init__(self, piece, rectangle):
        pygame.sprite.Sprite.__init__(self)

        self.piece = piece

        rect = pygame.Rect(rectangle)

        self.sprite_sheet = pygame.image.load('examples/guichess/resources/chess_pieces.png')

        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        image.blit(self.sprite_sheet, (0, 0), rect)

        self.image = pygame.transform.smoothscale(image, self.piece.board.get_square_dimensions())

        self.rect = pygame.Rect(self.piece.board.position_to_surface_position(self.piece.position) +
                                self.piece.board.get_square_dimensions())

        self.selected = 0
        self.mouse_drag = False

    def update(self, *args):
        if not self.mouse_drag:
            self.rect = pygame.Rect(self.piece.board.position_to_surface_position(self.piece.position) +
                                    self.piece.board.get_square_dimensions())

    def valid_destination(self, pos):
        for m in self.piece.moves():
            converted_pos = self.piece.board.surface_position_to_position(pos)
            if m.destination == converted_pos:
                return m

        return None

    def on_mouse_button_down(self):
        self.mouse_drag = True

        x, y = pygame.mouse.get_pos()

        if self.rect.collidepoint(x, y):
            self.selected += 1

            if self.selected > 1:
                self.selected = 0
        else:
            self.selected = False

    def on_mouse_button_up(self):
        if self.selected:
            move = self.valid_destination(pygame.mouse.get_pos())

            if move:
                self.piece.board.move(move)
                self.selected = 0
                self.piece.board.game.next_player()
            else:
                self.selected = 1

        self.mouse_drag = False

    def on_mouse_move(self):
        if self.selected and self.mouse_drag:
            pygame.mouse.set_pos(self.rect.centerx, self.rect.centery)
            x, y = pygame.mouse.get_pos()
            size = int(self.piece.board.get_square_size() / 2)
            pos = x - size, y - size
            self.rect = pygame.Rect(pos + self.piece.board.get_square_dimensions())


class GuiKing(pychess.pieces.King, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.King.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiQueen(pychess.pieces.Queen, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Queen.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiRook(pychess.pieces.Rook, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Rook.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiBishop(pychess.pieces.Bishop, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Bishop.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiKnight(pychess.pieces.Knight, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Knight.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))


class GuiPawn(pychess.pieces.Pawn, GuiPiece):
    def __init__(self, board, pos, c):
        pychess.pieces.Pawn.__init__(self, board, pos, c)
        GuiPiece.__init__(self, self, SpriteSheetPositions[self.type][self.color] + (SpriteSize, SpriteSize))
