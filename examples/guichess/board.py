# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

import pygame
import pychess

from pychess import PieceColor, MoveTypes
from examples.guichess.pieces import GuiKing, GuiQueen, GuiRook, GuiBishop, GuiKnight, GuiPawn


class GuiBoard(pychess.board.StandardBoard):
    def __init__(self, player, size, offset=(0, 0), colors=((240, 217, 217), (142, 100, 100))):
        pychess.board.StandardBoard.__init__(self)

        self.player = player

        self.offset = offset

        self.surface = pygame.Surface(size)

        self.colors = colors

        self.pieces.clear()

        self.pieces = {(4, 0): GuiKing(self, (4, 0), PieceColor.WHITE),
                       (4, 7): GuiKing(self, (4, 7), PieceColor.BLACK),
                       (3, 0): GuiQueen(self, (3, 0), PieceColor.WHITE),
                       (3, 7): GuiQueen(self, (3, 7), PieceColor.BLACK),
                       (0, 0): GuiRook(self, (0, 0), PieceColor.WHITE),
                       (7, 0): GuiRook(self, (7, 0), PieceColor.WHITE),
                       (0, 7): GuiRook(self, (0, 7), PieceColor.BLACK),
                       (7, 7): GuiRook(self, (7, 7), PieceColor.BLACK),
                       (2, 0): GuiBishop(self, (2, 0), PieceColor.WHITE),
                       (5, 0): GuiBishop(self, (5, 0), PieceColor.WHITE),
                       (2, 7): GuiBishop(self, (2, 7), PieceColor.BLACK),
                       (5, 7): GuiBishop(self, (5, 7), PieceColor.BLACK),
                       (1, 0): GuiKnight(self, (1, 0), PieceColor.WHITE),
                       (6, 0): GuiKnight(self, (6, 0), PieceColor.WHITE),
                       (1, 7): GuiKnight(self, (1, 7), PieceColor.BLACK),
                       (6, 7): GuiKnight(self, (6, 7), PieceColor.BLACK)}

        for i in range(0, 8):
            self.pieces[(i, 1)] = GuiPawn(self, (i, 1), PieceColor.WHITE)
            self.pieces[(i, 6)] = GuiPawn(self, (i, 6), PieceColor.BLACK)

    def next_player(self):
        self.player = pychess.PieceColor.BLACK if self.player == pychess.PieceColor.WHITE else pychess.PieceColor.WHITE

    def handle_event(self, event):
        relevant_pieces = self.get_all_pieces(self.player)

        for rp in relevant_pieces:
            if event.type == pygame.MOUSEBUTTONDOWN:
                rp.on_mouse_button_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                rp.on_mouse_button_up(event)
            elif event.type == pygame.MOUSEMOTION:
                rp.on_mouse_move(event)

    def render(self):
        square_size = self.get_square_size()

        file_diff = self.get_top_right()[0] - self.get_bottom_left()[0]
        rank_diff = self.get_top_right()[1] - self.get_bottom_left()[0]

        for y in reversed(range(0, rank_diff + 1)):
            for x in range(0, file_diff + 1):
                current_square = (square_size * x, square_size * y, square_size, square_size)
                if x % 2 == 0 and y % 2 == 0 or x % 2 == 1 and y % 2 == 1:
                    pygame.draw.rect(self.surface, self.colors[0], current_square)
                else:
                    pygame.draw.rect(self.surface, self.colors[1], current_square)

        selected_piece = None

        for _, s in self.pieces.items():
            s.update()

            if s.selected:
                selected_piece = s
                self.render_highlight_squares(s)

            if s.is_king() and s.in_check():
                self.render_highlight_square(s.position, color=(255, 0, 0), alpha=150)

            last_move = self.get_last_move()
            if last_move:
                self.render_highlight_square(last_move.origin, color=(133, 135, 6), alpha=10)
                self.render_highlight_square(last_move.destination, color=(133, 135, 6), alpha=10)

            self.surface.blit(s.image, s.rect)

        if selected_piece:
            self.surface.blit(selected_piece.image, selected_piece.rect)

        return self.surface

    def render_highlight_squares(self, piece):
        self.render_highlight_square(piece.position, color=(20, 135, 0), alpha=150)

        for m in piece.moves():
            self.render_highlight_square(m.destination, color=(20, 135, 0), alpha=80, type=m.type)

    def render_highlight_square(self, square, color=(78, 244, 66), alpha=70, type=None):
        color_key = (127, 33, 33)

        size = self.get_square_size()

        square_surface = pygame.Surface(self.get_square_dimensions())
        square_surface.fill(color_key)
        square_surface.set_colorkey(color_key)

        if type == MoveTypes.CAPTURE:
            pygame.draw.rect(square_surface, color, (0, 0, size, size))

            center = int(size / 2)
            pygame.draw.circle(square_surface, (255, 0, 0), (center, center), int(size * 0.55))

            square_surface.set_colorkey((255, 0, 0))
        elif type in [MoveTypes.MOVE, MoveTypes.SHORT_CASTLE, MoveTypes.LONG_CASTLE]:
            center = int(size / 2)
            pygame.draw.circle(square_surface, color, (center, center), int(size * 0.14))
        else:
            pygame.draw.rect(square_surface, color, (0, 0, size, size))

        square_surface.set_alpha(alpha)

        surface_position = self.position_to_surface_position(square)
        self.surface.blit(square_surface, surface_position + self.get_square_dimensions())

    def get_square_dimensions(self):
        x_squares = self.get_top_right()[0] - self.get_bottom_left()[0] + 1
        y_squares = self.get_top_right()[1] - self.get_bottom_left()[0] + 1

        size = min(self.surface.get_size()) / max(x_squares, y_squares)
        size = int(size)

        return size, size

    def get_square_size(self):
        return min(self.get_square_dimensions())

    def position_to_surface_position(self, position):
        x, y = position
        size = self.get_square_size()

        rank_max = (self.get_top_right()[1] - self.get_bottom_left()[0]) * size

        return (x * size), rank_max - (y * size)

    def surface_position_to_position(self, position):
        px, py = position

        x_offset, y_offset = self.offset

        px -= x_offset
        py -= y_offset

        file_diff = self.get_top_right()[0] - self.get_bottom_left()[0]
        rank_diff = self.get_top_right()[1] - self.get_bottom_left()[0]

        for y in reversed(range(0, rank_diff + 1)):
            for x in range(0, file_diff + 1):
                rect = pygame.Rect(self.position_to_surface_position((x, y)) + self.get_square_dimensions())

                if rect.collidepoint(px, py):
                    return x, y

        return -1, -1


