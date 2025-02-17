#Empezamos estableciendo las variables globales 'col' y 'row'
col = 'abcdefgh'
row = '12345678'

# Creamos un tablero
class Board:
        
    def __init__(self):
        self.board_squares = [[None for _ in range(8)] for _ in range(8)]

# Creamos las piezas
class Piece:

    def __init__(self, color, shown_position):
        """Possible attributes:

        Args:
            color (str): "white" or "black"
            shown_position (str): position on board following this display 'column' as a letter and 'row' as a number 

        """
        self.color = color
        self.position = col.index(shown_position[0]), row.index(shown_position[1])


    def move(self):
        
        if self.piecetype == 'Rook':
        #horizontal_move(self.position)
            print("I'm a Rook!")
        

    def moves_allow():
        pass

    #piecetype: "king", "queen", "rook", "knight", "bishop", "pawn"
class Rook(Piece):
        def __init__(self, color, shown_position, piecetype="Rook"):
            super().__init__(color, shown_position)
            self.piecetype = piecetype
              

Ra1 = Rook("w", "a1")
Ra1.move()