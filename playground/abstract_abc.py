from abc import ABC, abstractmethod


# abstract base class
# SOLID - is used for D principle.

class ChessPiece(ABC):

    def draw(self):
        print("Draw a chess piece.")

    @abstractmethod
    def move(self):
        pass


class Pawn(ChessPiece):

    def __int__(self):
        self.x = 10

    def move(self):
        pass


p = ChessPiece()
