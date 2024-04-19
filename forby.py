"""
Forby - stores a connect 4 board

DATA:
- 2d list board (O = p1, X = p2) {get;}

FUNCTIONALITY:
- Take in game string "3354" -> board
- Create a demo board, with a move in 
- Find next player to play
"""
class Forby:
    def __init__(self):
        self.__board__ = [[None for i in range(7)] for i in range(6)]
        print("I put the new forbys on the jeep")
    
    # Board getter
    def Board(self) -> list:
        return self.__board__
    
    """
    Parses input game string into board object
    INPUT str game string "34212"
    Parses string (if invalid, sets list to ["Invalid!"])
    """
    def Parse(self, game: str):
        # If there's a non-number in the game string, it must be invalid!
        if not game.isnumeric(): 
            self.__board__ = ["Invalid! Game string contains non-number(s) [#01]"]
            return
        
        # Clear board, set player to p1
        self.__board__ = [[None for i in range(7)] for i in range(6)]
        player = "O"
        for move in game:
            # Since c4 notation starts at 1, -1 for correct list indexes
            move = int(move)
            if move < 1 or move > 7: return ["Invalid! Invalid position [#02]"]
            x = move - 1
            # Find lowest position stone at x would drop to
            for y in range(5, -1, -1):
                if self.__board__[y][x] is None: 
                    self.__board__[y][x] = player
                    break
            # If no space in column, board must be invalid
            else:
                self.__board__ = ["Invalid! Column full [#03]"]
                return
            # Flip player's turn
            if player == "X": player = "O"
            else: player = "X"
    
    """
    Creates a demo board, with a stone placed in a position
    INPUT int x (1-6), player (1/2)
    RETURNS demo board, with stone placed in column x
    """
    def Demo(self, position: int, player: int) -> list:

        # Convert player to piece type
        if player == 1: player = "O"
        elif player == 2: player = "X"
        else: # Invalid player input (no p1/p2)
            return ["Invalid! Invalid player [#04]"]
        
        # Find lowest position stone at x would drop to
        if position < 1 or position > 7: return ["Invalid! Invalid position [#05]"]
        x = position - 1

        for y in range(5, -1, -1):
            if self.__board__[y][x] is None:
                self.__board__[y][x] = player
                break
        else:
            return ["Invalid! Column full [#06]"]
        return self.__board__
    
    """
    Finds who is next player to player
    INPUT -
    RETURNS int next player (O=1, X=2, invalid=-1) 
    """
    def NextPlayer(self) -> int:
        O = 1
        X = 2
        xCount = 0
        oCount = 0
        # For each row in board, add number of O/Xs to count
        for row in self.__board__:
            oCount += row.count("O")
            xCount += row.count("X")
        # If one player has >1 stones on board than the other, board must be invalid
        if abs(xCount - oCount) > 1: return -1
        # Return whichever one is higher
        else: return X if oCount > xCount else O




            

    
