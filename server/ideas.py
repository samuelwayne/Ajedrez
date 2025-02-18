#Empezamos estableciendo las variables globales 'col' y 'row'
col = 'abcdefgh'
row = '12345678'

# Creamos un tablero
class Square():
    
    def __init__(self, position, occupied=False):
        """Objet square

        Args:
            position (tuple): (x, y) as indexing coordinates
            occupied (bool, optional): Piece occupying. Defaults to False for free squares.
        """
        self.position = position
        self.occupied = occupied

class Board:
        
    def __init__(self, size=(8, 8)):
        """Board object

        Args:
            size (tuple, optional): Length, width of the board created. Defaults to (8, 8), common chess board.
        """
        self.size = size
        #board creation
        position_coordinates = [[(x, y) for y in range(self.size[1])] for x in range(self.size[0])]
        self.list_position_coordinates = []
        [self.list_position_coordinates.extend(element) for element in position_coordinates]
        position_names = [[col[x]+str(y+1) for y in range(self.size[1])] for x in range(self.size[0])]
        self.list_position_names = []
        [self.list_position_names.extend(element) for element in position_names]
       
    def create_new_board (self):
        self.board = dict(map(lambda x, y: (x, y), self.list_position_names, self.list_position_coordinates))
        return self.board

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
board = Board()
board.create_new_board()
print(board.board)
