#Empezamos estableciendo las variables globales 'col' y 'row'
col = 'abcdefgh'
row = '12345678'

class Board:
        
    def __init__(self, size=(8, 8)):
        """Board object

        Args:
            size (tuple, optional): Length, width of the board created. Defaults to (8, 8), common chess board.
        """
        self.size = size

    #creating board tuple positions
        position_coordinates = [[(x, y) for y in range(self.size[1])] for x in range(self.size[0])]
        #unrolling list in a list into a plain list
        self.list_position_coordinates = []
        [self.list_position_coordinates.extend(coords) for coords in position_coordinates]

    #creating board names "a1" type
        position_names = [[col[x]+str(y+1) for y in range(self.size[1])] for x in range(self.size[0])]
        #unrolling list in a list into a plain list
        self.list_position_names = []
        [self.list_position_names.extend(element) for element in position_names]

    #creating occupied state as False by default
        occupied = False
        self.list_occupied_state = [occupied for _ in range(self.size[0]*self.size[1])]
       
    def create_new_board (self):
        #everything into a dictionary
        self.board = dict(map(lambda x, y, z: (x, [y, z]), self.list_position_coordinates, self.list_position_names, self.list_occupied_state))
        return self.board


class Piece:

    def __init__(self, color, shown_position, board):
        """Possible attributes:

        Args:
            color (str): "white" or "black"
            shown_position (str): position on board following this display 'column' as a letter and 'row' as a number 

        """
        self.color = color
        self.position = col.index(shown_position[0]), row.index(shown_position[1])
        board.board[self.position][1] = color

    def moves_allow(self, board):
        #We define the current self.position and board.size by spliting x and y components,
        # and create an empty list for the results
        x_piece, y_piece = self.position
        x_size, y_size = board.size
        list_moves_allow = []
        if "horizontal" in self.move_type:
            for x in range(x_piece-1, -1, -1):
                #Adding squares allowed compared within the ROW in which we have the piece in one direction
                #Also checked if the piece is black or white to know if it can either be eaten or unoccupied
                if board.board[(x, y_piece)][1] == self.color:
                    break
                elif board.board[(x, y_piece)][1] == False:
                    list_moves_allow.append((x, y_piece))
                else:
                    list_moves_allow.append((x, y_piece))
                    break
            for x in range(x_piece+1, x_size):
                #Adding squares allowed compared within the ROW in which we have the piece in the other direction
                #Also checked if the piece is black or white to know if it can either be eaten or unoccupied
                if board.board[(x, y_piece)][1] == self.color:
                    break
                elif board.board[(x, y_piece)][1] == False:
                    list_moves_allow.append((x, y_piece))
                else:
                    list_moves_allow.append((x, y_piece))
                    break
            for y in range(y_piece-1, -1, -1):
                #Adding squares allowed compared within the COLUMN in which we have the piece in one direction
                #Also checked if the piece is black or white to know if it can either be eaten or unoccupied
                if board.board[(x_piece, y)][1] == self.color:
                    break
                elif board.board[(x_piece, y)][1] == False:
                    list_moves_allow.append((x_piece, y))
                else:
                    list_moves_allow.append((x_piece, y))
                    break
            for y in range(y_piece+1, y_size):
                #Adding squares allowed compared within the COLUMN in which we have the piece in the other direction
                #Also checked if the piece is black or white to know if it can either be eaten or unoccupied
                if board.board[(x_piece, y)][1] == self.color:
                    break
                elif board.board[(x_piece, y)][1] == False:
                    list_moves_allow.append((x_piece, y))
                else:
                    list_moves_allow.append((x_piece, y))

        return list_moves_allow
                

    def move(self):
    
        if self.piecetype == 'Rook':
        #horizontal_move(self.position)
            return print("Here will come the piece of code that actually moves the piece")
        

    #piecetype: "king", "queen", "rook", "knight", "bishop", "pawn"
class Rook(Piece):
        def __init__(self, color, shown_position, board, piecetype="Rook", move_type=["horizontal"]):
            super().__init__(color, shown_position, board)
            self.piecetype = piecetype
            self.move_type = move_type
              
board1 = Board()
board1.create_new_board()
R1 = Rook("w", "b2", board1)
R2 = Rook("w", "b5", board1)
R3 = Rook("b", "c2", board1)
print(R1.position)
print(R2.position)
print(R3.position)
print(R1.moves_allow(board1))
print(R2.moves_allow(board1))
print(R3.moves_allow(board1))