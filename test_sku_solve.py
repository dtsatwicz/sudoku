import unittest

#from sku_solve import xxcells_in_row
#from sku_solve import cells_in_row
#from sku_solve import __main__
#from sku_solve import main
#target = __import__("sku_solve.py")
#target = __import__("sku_solve")
target = __import__("sku_solve")

class TestCellsInRow(unittest.TestCase):
    def test_cells_in_row(self):
        """
        Test that correct list of cells in as row are returned
        """
        data = 1
        result = target.cells_in_row(data) # module 'sku_solve' has no attribute cells_in_row
        #result = target.main.cells_in_row(data) # module 'sku_solve has no attribute main
        #result = target.__main__.cells_in_row(data)
        #result = target.xxcells_in_row(data) #this works but xxcells_in_row is outside main

        correct_result = [0,9,18,27,36,45,54,63,72]
        self.assertEqual (result, correct_result)

if __name__ == '__main__':
    unittest.main()
    pass
