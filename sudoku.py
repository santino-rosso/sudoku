class NumberExistingInTheRow(Exception):
    pass

class NumberExistingInTheCol(Exception):
    pass

class NumberExistingInTheZone(Exception):
    pass


class Sudoku:

    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def insert(self, row, col, number):
        self.check_row_and_col(row,col,number)
        self.check_zone(row,col,number)
        self.board[row][col] = number

    def remove(self,row,col):
        self.board[row][col] = 0

    def check_row_and_col(self,row,col,number):
        for x in range(9):
            if self.board[x][col] == number and x!= row:
                raise NumberExistingInTheCol()
        
        for y in range(9):
            if self.board[row][y] == number and y != col:
                raise NumberExistingInTheRow()
    
    def check_zone(self,row,col,number):
        for x in self.zone_row(row):
            for y in self.zone_col(col):
                if self.board[x][y] == number and ( x!=row and y!=col):
                    raise NumberExistingInTheZone()

    def zone_row(self,row):
        if(row // 3) * 3 == 0:
            return [0,1,2]
        if(row // 3) * 3 == 3:
            return [3,4,5]
        if(row // 3) * 3 == 6:
            return [6,7,8]
    
    def zone_col(self,col):
        if(col // 3) * 3 == 0:
            return [0,1,2]
        if(col // 3) * 3 == 3:
            return [3,4,5]
        if(col // 3) * 3 == 6:
            return [6,7,8]