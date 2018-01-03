# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#
# Just for fun xmas 2017 chess project
#

import general
from pieces import Pawn, Rook, King, Queen, Knight, Bishop


class Board:
    def __init__(self):
        self._history = []
        self.pieces = {(4, 0): King(self, (4, 0), 'light'), (4, 7): King(self, (4, 7), 'dark'),
                       (3, 0): Queen(self, (3, 0), 'light'), (3, 7): Queen(self, (3, 7), 'dark'),
                       (0, 0): Rook(self, (0, 0), 'light'), (7, 0): Rook(self, (7, 0), 'light'),
                       (0, 7): Rook(self, (0, 7), 'dark'), (7, 7): Rook(self, (7, 7), 'dark'),
                       (2, 0): Bishop(self, (2, 0), 'light'), (5, 0): Bishop(self, (5, 0), 'light'),
                       (2, 7): Bishop(self, (2, 7), 'dark'), (5, 7): Bishop(self, (5, 7), 'dark'),
                       (1, 0): Knight(self, (1, 0), 'light'), (6, 0): Knight(self, (6, 0), 'light'),
                       (1, 7): Knight(self, (1, 7), 'dark'), (6, 7): Knight(self, (6, 7), 'dark')}

        for i in range(0, 8):
            self.pieces[(i, 1)] = Pawn(self, (i, 1), 'light')
            self.pieces[(i, 6)] = Pawn(self, (i, 6), 'dark')

    def get_pieces(self):
        return self.pieces

    def pieces_by_color(self, color):
        result = []

        for pos, piece in self.pieces.items():
            if piece.color == color and piece.type != 'King':
                result.append(piece)
        return result

    def filter_pieces(self, piece_type=None, piece_color=None):
        filtered = []

        for _, p in self.pieces.items():
            if piece_type and piece_type != p.type:
                continue
            if piece_color and piece_color != p.color:
                continue

            filtered.append(p)

        return filtered

    def light_pieces(self):
        return [p for p in self.filter_pieces(piece_color='light') if p.type != 'King']

    def dark_pieces(self):
        return [p for p in self.filter_pieces(piece_color='dark') if p.type != 'King']

    def get_king(self, color):
        return self.filter_pieces('King', color)[0]

    def get_light_king(self):
        return self.filter_pieces('King', 'light')[0]

    def get_dark_king(self):
        return self.filter_pieces('King', 'dark')[0]

    def get_light_queens(self):
        return self.filter_pieces('Queen', 'light')

    def get_dark_queens(self):
        return self.filter_pieces('Queen', 'dark')

    def get_light_rooks(self):
        return self.filter_pieces('Rook', 'light')

    def get_dark_rooks(self):
        return self.filter_pieces('Rook', 'dark')

    def get_light_bishops(self):
        return self.filter_pieces('Bishop', 'light')

    def get_dark_bishops(self):
        return self.filter_pieces('Bishop', 'dark')

    def get_light_knights(self):
        return self.filter_pieces('Knight', 'light')

    def get_dark_knights(self):
        return self.filter_pieces('Knight', 'dark')

    def my_king(self, p):
        return self.get_light_king() if p.light() else self.get_dark_king()

    def enemy_king(self, p):
        return self.get_dark_king() if p.light() else self.get_light_king()

    def king_side_rook(self, color):
        if color == 'light':
            if (7, 0) in self.pieces and self.pieces[(7, 0)].type == 'Rook' and self.pieces[(7, 0)].color == color:
                return self.pieces[(7, 0)]
        else:
            if (7, 7) in self.pieces and self.pieces[(7, 7)].type == 'Rook' and self.pieces[(7, 7)].color == color:
                return self.pieces[(7, 7)]

    def queen_side_rook(self, color):
        if color == 'light':
            if (0, 0) in self.pieces and self.pieces[(0, 0)].type == 'Rook' and self.pieces[(0, 0)].color == color:
                return self.pieces[(0, 0)]
        else:
            if (0, 7) in self.pieces and self.pieces[(0, 7)].type == 'Rook' and self.pieces[(0, 7)].color == color:
                return self.pieces[(0, 7)]

    def history(self):
        return self._history

    def move(self, move):
        if not move:
            raise RuntimeError('board.move(piece, move): could not make the move!')

        move.piece.history().append(move)

        if move.type == 'Capture':
            # remove captured piece
            self.pieces.pop(move.captured_piece.position)

            piece = self.pieces.pop(move.piece.position)

            piece.position = move.destination
            self.pieces[move.destination] = piece
        elif move.type in ['Promotion', 'Capture Promotion']:
            self.promote(move)
        elif move.type in ['King Side Castle', 'Queen Side Castle']:
            rook = self.pieces.pop(move.rook.position)
            # add move also to rook history
            rook.history().append(move)

            king = self.pieces.pop(move.king.position)

            rook.position = move.rook_destination
            king.position = move.destination

            self.pieces[rook.position] = rook
            self.pieces[king.position] = king
        else:
            piece = self.pieces.pop(move.piece.position)

            piece.position = move.destination
            self.pieces[move.destination] = piece

        self._history.append(move)

        return move

    def promote(self, move):
        if move.type not in ['Promotion', 'Capture Promotion']:
            raise RuntimeError('board.promote(move): not a promotion move!')

        new_piece = move.promoted_piece_name

        if new_piece not in ['Queen', 'Rook', 'Knight', 'Bishop']:
            raise RuntimeError('board.promote(move): unknown piece: ' + new_piece)

        if move.piece.type == 'Pawn' and self.second_last_rank(move.piece):
            color = move.piece.color
            pos = move.destination

            if new_piece == 'Queen':
                new_piece = Queen(self, pos, color)
            elif new_piece == 'Rook':
                new_piece = Rook(self, pos, color)
            elif new_piece == 'Bishop':
                new_piece = Bishop(self, pos, color)
            elif new_piece == 'Knight':
                new_piece = Knight(self, pos, color)

            if move.type == 'Capture Promotion':
                # remove captured piece
                self.pieces.pop(move.captured_piece.position)

            self.pieces.pop(move.piece.position)  # remove pawn
            self.pieces[pos] = new_piece

            move.promoted_piece = new_piece

    def pieces_between(self, p1, p2):
        p1_x, p1_y, p2_x, p2_y = self.get_coordinates(p1, p2)

        pieces = []

        if self.same_rank(p1, p2):
            for x in range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x)):
                if (x, p1_y) in self.pieces:
                    pieces.append(self.pieces[(x, p1_y)])
            return pieces
        elif self.same_file(p1, p2):
            for y in range(min(p1_y + 1, p2_y + 1), max(p1_y, p2_y)):
                if (p1_x, y) in self.pieces:
                    pieces.append(self.pieces[(p1_x, y)])
            return pieces
        elif self.same_diagonal(p1, p2):
            y = min(p1_y + 1, p2_y + 1)
            x_range = range(min(p1_x + 1, p2_x + 1), max(p1_x, p2_x))

            if self.same_falling_diagonal(p1, p2):
                x_range = reversed(x_range)

            for x in x_range:
                if (x, y) in self.pieces:
                    pieces.append(self.pieces[(x, y)])
                y += 1

            return pieces
        else:
            return []

    def get_move_squares(self, p, direction, limit=None):
        try:
            p_x, p_y = p.position
        except AttributeError:
            p_x, p_y = p

        if limit:
            try:
                limit_x, limit_y = limit.position
            except AttributeError:
                limit_x, limit_y = limit
        else:
            limit_x = limit_y = None

        squares = []
        color = 1 if p.light() else -1

        if direction == general.MoveDirection.RankUp:
            rank_up_range = range(p_y + 1, 8) if p.light() else reversed(range(0, p_y))
            for y in rank_up_range:
                squares.append((p_x, y))
                if (p_x, y) in self.pieces or (limit_x, limit_y) == (p_x, y):
                    break
        elif direction == general.MoveDirection.RankDown:
            rank_down_range = reversed(range(0, p_y)) if p.light() else range(p_y + 1, 8)
            for y in rank_down_range:
                squares.append((p_x, y))
                if (p_x, y) in self.pieces or (limit_x, limit_y) == (p_x, y):
                    break
        elif direction == general.MoveDirection.FileRight:
            file_right_range = range(p_x + 1, 8) if p.light() else reversed(range(max(p_x - 1, 0), 0))
            for x in file_right_range:
                squares.append((x, p_y))
                if (x, p_y) in self.pieces or (limit_x, limit_y) == (x, p_y):
                    break
        elif direction == general.MoveDirection.FileLeft:
            file_left_range = reversed(range(0, p_x)) if p.light() else range(p_x + 1, 8)
            for x in file_left_range:
                squares.append((x, p_y))
                if (x, p_y) in self.pieces or (limit_x, limit_y) == (x, p_y):
                    break
        elif direction == general.MoveDirection.RisingDiagonalUp:
            y = p_y + 1 * color
            rising_diagonal_up_range = range(p_x + 1, 8) if p.light() else reversed(range(0, p_x))
            for x in rising_diagonal_up_range:
                if not 0 <= y <= 7:
                    break

                squares.append((x, y))
                if (x, y) in self.pieces or (limit_x, limit_y) == (x, y):
                    break
                y += 1 * color
        elif direction == general.MoveDirection.RisingDiagonalDown:
            y = p_y - 1 * color
            rising_diagonal_down_range = reversed(range(0, p_x)) if p.light() else range(p_x + 1, 8)
            for x in rising_diagonal_down_range:
                if not 0 <= y <= 7:
                    break

                squares.append((x, y))
                if (x, y) in self.pieces or (limit_x, limit_y) == (x, y):
                    break
                y -= 1 * color
        elif direction == general.MoveDirection.FallingDiagonalUp:
                y = p_y + 1 * color
                falling_diagonal_up_range = reversed(range(0, p_x)) if p.light() else range(p_x + 1, 8)
                for x in falling_diagonal_up_range:
                    if not 0 <= y <= 7:
                        break

                    squares.append((x, y))
                    if (x, y) in self.pieces or (limit_x, limit_y) == (x, y):
                        break
                    y += 1 * color
        elif direction == general.MoveDirection.FallingDiagonalDown:
                y = p_y - 1 * color
                rising_diagonal_down_range = range(p_x + 1, 8) if p.light() else reversed(range(0, p_x))
                for x in rising_diagonal_down_range:
                    if not 0 <= y <= 7:
                        break

                    squares.append((x, y))
                    if (x, y) in self.pieces or (limit_x, limit_y) == (x, y):
                        break
                    y -= 1 * color

        return squares

    def rank_pin(self, piece):
        return self.rank_pin_piece(piece) is not None

    def rank_pin_piece(self, piece):
        king = self.get_light_king() if piece.light() else self.get_dark_king()

        if self.same_rank(king, piece) and len(self.pieces_between(king, piece)) == 0:
            rooks = self.get_dark_rooks() if piece.light() else self.get_light_rooks()
            queens = self.get_dark_queens() if piece.light() else self.get_light_queens()

            for r in rooks:
                if self.same_rank(r, piece) and len(self.pieces_between(r, piece)) == 0:
                    return r

            for q in queens:
                if self.same_rank(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return q
        else:
            return None

    def file_pin(self, piece):
        return self.file_pin_piece(piece) is not None

    def file_pin_piece(self, piece):
        king = self.get_light_king() if piece.light() else self.get_dark_king()

        if self.same_file(king, piece) and len(self.pieces_between(king, piece)) == 0:
            rooks = self.get_dark_rooks() if piece.light() else self.get_light_rooks()
            queens = self.get_dark_queens() if piece.light() else self.get_light_queens()

            for r in rooks:
                if self.same_file(r, piece) and len(self.pieces_between(r, piece)) == 0:
                    return r

            for q in queens:
                if self.same_file(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return q

        return None

    def diagonal_pin(self, piece):
        return self.diagonal_pin_piece(piece) is not None

    def diagonal_pin_piece(self, piece):
        king = self.get_light_king() if piece.light() else self.get_dark_king()

        if self.same_rising_diagonal(king, piece) and len(self.pieces_between(king, piece)) == 0:
            bishops = self.get_dark_bishops() if piece.light() else self.get_light_bishops()
            queens = self.get_dark_queens() if piece.light() else self.get_light_queens()

            for b in bishops:
                if self.same_rising_diagonal(b, piece) and len(self.pieces_between(b, piece)) == 0:
                    return b

            for q in queens:
                if self.same_rising_diagonal(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return q

        elif self.same_falling_diagonal(king, piece) and len(self.pieces_between(king, piece)) == 0:
            bishops = self.get_dark_bishops() if piece.light() else self.get_light_bishops()
            queens = self.get_dark_queens() if piece.light() else self.get_light_queens()

            for b in bishops:
                if self.same_falling_diagonal(b, piece) and len(self.pieces_between(b, piece)) == 0:
                    return b

            for q in queens:
                if self.same_falling_diagonal(q, piece) and len(self.pieces_between(q, piece)) == 0:
                    return q

        return None

    def protected_square(self, square, protected_by_color):
        for s, p in self.pieces.items():
            if p.color == protected_by_color:
                for i in p.influenced_squares():
                    if i == square:
                        return True
        return False

    @staticmethod
    def enemy_color(p):
        return 'dark' if p.light() else 'light'

    @staticmethod
    def first_rank(p):
        return p.position[1] == 0 if p.light() else p.position[1] == 7

    @staticmethod
    def last_rank(p):
        return p.position[1] == 7 if p.light() else p.position[1] == 0

    @staticmethod
    def second_last_rank(p):
        return p.position[1] == 6 if p.light() else p.position[1] == 1

    @staticmethod
    def en_passant_rank(p):
        return p.position[1] == 4 if p.light() else p.position[1] == 3

    @staticmethod
    def king_side_castle_positions(color):
        if color == 'light':
            return (6, 0), (5, 0)
        else:
            return (6, 7), (5, 7)

    @staticmethod
    def queen_side_castle_positions(color):
        if color == 'light':
            return (2, 0), (3, 0)
        else:
            return (2, 7), (3, 7)

    @staticmethod
    def get_coordinates(p1, p2):
        try:
            p1_x, p1_y = p1.position
        except AttributeError:
            p1_x, p1_y = p1

        try:
            p2_x, p2_y = p2.position
        except AttributeError:
            p2_x, p2_y = p2

        return p1_x, p1_y, p2_x, p2_y

    @staticmethod
    def same_rank(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)
        return p1_y == p2_y

    @staticmethod
    def same_file(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)
        return p1_x == p2_x

    @staticmethod
    def same_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)

        # y = kx+d ... d = yi - xi
        falling = p1_y == p1_x + p2_y - p2_x
        rising = p1_y == -p1_x + p2_y + p2_x

        return falling or rising

    @staticmethod
    def same_rising_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)

        return p1_y == -p1_x + p2_y + p2_x

    @staticmethod
    def same_falling_diagonal(p1, p2):
        p1_x, p1_y, p2_x, p2_y = Board.get_coordinates(p1, p2)

        return p1_y == p1_x + p2_y - p2_x

    @staticmethod
    def in_board(x, y):
        return 0 <= x < 8 and 0 <= y < 8
