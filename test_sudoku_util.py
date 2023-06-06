import unittest

#class SudokuUtil():
#    import sudoku_util as su
#sudoku_util = SudokuUtil()
import sudoku_util as su

class TestCellsInRow(unittest.TestCase):
    def test1_cells_in_row(self):
        """
        Test that correct list of cells in as row are returned
        """
        data = 1
        #result = target.cells_in_row(data) # module 'sudoku_util' has no attribute cells_in_row
        #result = sudoku_util.su.cells_in_row(data) # module 'sudoku_util' has no attribute cells_in_row
        result = su.cells_in_row(data) # module 'sudoku_util' has no attribute cells_in_row

        correct_result = [9,0,9,18,27,36,45,54,63,72]
        self.assertNotEqual (result, correct_result)
        
    def test2_cells_in_row(self):
        """
        Test that correct list of cells in as row are returned
        """
        data = 2
        #result = target.cells_in_row(data) # module 'sudoku_util' has no attribute cells_in_row
        #result = sudoku_util.su.cells_in_row(data) # module 'sudoku_util' has no attribute cells_in_row
        result = su.cells_in_row(data) # module 'sudoku_util' has no attribute cells_in_row

        correct_result = [9,10,11,12,13,14,15,16,17]
        self.assertEqual (result, correct_result)
