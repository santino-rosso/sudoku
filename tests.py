import unittest
from sudoku import Sudoku, NumberExistingInTheRow, NumberExistingInTheCol, NumberExistingInTheZone


class TestSudoku(unittest.TestCase):
    
    def test_create_board(self):
        sudoku = Sudoku()
        self.assertEqual(len(sudoku.board), 9)
        self.assertEqual(len(sudoku.board[0]), 9)

    def test_set_number_basic(self):
        sudoku = Sudoku()
        sudoku.insert(1, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)

    def test_set_number_validate_column(self):
        sudoku = Sudoku()
        sudoku.insert(1, 1, 9)
        with self.assertRaises(NumberExistingInTheCol):
            sudoku.insert(2, 1, 9)
    
    def test_set_number_validate_row(self):
        sudoku = Sudoku()
        sudoku.insert(1, 1, 9)
        with self.assertRaises(NumberExistingInTheRow):
            sudoku.insert(1, 2, 9)

    def test_set_number_validate_zone0(self):
        sudoku = Sudoku()
        sudoku.insert(1, 1, 9)
        with self.assertRaises(NumberExistingInTheZone):
            sudoku.insert(2, 2, 9)

    def test_set_number_validate_zone1(self):
        sudoku = Sudoku()
        sudoku.insert(3, 4, 9)
        with self.assertRaises(NumberExistingInTheZone):
            sudoku.insert(5, 5, 9)

    def test_set_number_validate_zone2(self):
        sudoku = Sudoku()
        sudoku.insert(6, 7, 9)
        with self.assertRaises(NumberExistingInTheZone):
            sudoku.insert(7, 6, 9)

    def test_remove_number(self):
        sudoku = Sudoku()
        sudoku.insert(1,1,9)
        sudoku.remove(1,1)
        self.assertEqual(sudoku.board[1][1],0)

if __name__ == '__main__':
    unittest.main()