# Mathias Punkenhofer
# code.mpunkenhofer@gmail.com
#

from pychess import PieceType, PieceColor

SpriteSize = 132

SpriteSheetPositions = {PieceType.ROOK: {PieceColor.WHITE: (0 * SpriteSize, 0),
                                         PieceColor.BLACK: (0 * SpriteSize, SpriteSize)},
                        PieceType.KNIGHT: {PieceColor.WHITE: (1 * SpriteSize, 0),
                                           PieceColor.BLACK: (1 * SpriteSize, SpriteSize)},
                        PieceType.BISHOP: {PieceColor.WHITE: (2 * SpriteSize, 0),
                                           PieceColor.BLACK: (2 * SpriteSize, SpriteSize)},
                        PieceType.QUEEN: {PieceColor.WHITE: (3 * SpriteSize, 0),
                                          PieceColor.BLACK: (3 * SpriteSize, SpriteSize)},
                        PieceType.KING: {PieceColor.WHITE: (4 * SpriteSize, 0),
                                         PieceColor.BLACK: (4 * SpriteSize, SpriteSize)},
                        PieceType.PAWN: {PieceColor.WHITE: (5 * SpriteSize, 0),
                                         PieceColor.BLACK: (5 * SpriteSize, SpriteSize)},
                        }
