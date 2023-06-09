# sudoku_util.py

def sudoku_values():  
            return ['1','2','3','4','5','6','7','8','9']
        
def cells_in_row(row):
            cells = [[],
                     [ 0, 1, 2, 3, 4, 5, 6, 7, 8],
                     [ 9,10,11,12,13,14,15,16,17],
                     [18,19,20,21,22,23,24,25,26],
                     [27,28,29,30,31,32,33,34,35],
                     [36,37,38,39,40,41,42,43,44],
                     [45,46,47,48,49,50,51,52,53],
                     [54,55,56,57,58,59,60,61,62],
                     [63,64,65,66,67,68,69,70,71],
                     [72,73,74,75,76,77,78,79,80],
                     ]
            return cells[row]
                     
def cells_in_col(col):
            cells = [[],
                     [ 0, 9,18,27,36,45,54,63,72],
                     [ 1,10,19,28,37,46,55,64,73],
                     [ 2,11,20,29,38,47,56,65,74],
                     [ 3,12,21,30,39,48,57,66,75],
                     [ 4,13,22,31,40,49,58,67,76],
                     [ 5,14,23,32,41,50,59,68,77],
                     [ 6,15,24,33,42,51,60,69,78],
                     [ 7,16,25,34,43,52,61,70,79],
                     [ 8,17,26,35,44,53,62,71,80],
                     ]
            return cells[col]
                     
def cells_in_box(box):
            cells = [[],
                     [ 0, 1, 2, 9,10,11,18,19,20],
                     [ 3, 4, 5,12,13,14,21,22,23],
                     [ 6, 7, 8,15,16,17,24,25,26],
                     [27,28,29,36,37,38,45,46,47],
                     [30,31,32,39,40,41,48,49,50],
                     [33,34,35,42,43,44,51,52,53], 
                     [54,55,56,63,64,65,72,73,74],
                     [57,58,59,66,67,68,75,76,77],
                     [60,61,62,69,70,71,78,79,80],
                     ]
            return cells[box]
                     
def rows_of_cell_index(cell_index):
            rows = [[],
                    [1,1,1,1,1,1,1,1,1],
                    [2,2,2,2,2,2,2,2,2],
                    [3,3,3,3,3,3,3,3,3],
                    [4,4,4,4,4,4,4,4,4],
                    [5,5,5,5,5,5,5,5,5],
                    [6,6,6,6,6,6,6,6,6],
                    [7,7,7,7,7,7,7,7,7],
                    [8,8,8,8,8,8,8,8,8],
                    [9,9,9,9,9,9,9,9,9],
                   ]
            return rows[cell_index]

def cols_of_cell_index(cell_index):
            cols = [[],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                   ]
            return cols[cell_index]

def boxs_of_cell_index(cell_index):
            boxs = [[],
                    [1,1,1,2,2,2,3,3,3],
                    [1,1,1,2,2,2,3,3,3],
                    [1,1,1,2,2,2,3,3,3],
                    [4,4,4,5,5,5,6,6,6],
                    [4,4,4,5,5,5,6,6,6],
                    [4,4,4,5,5,5,6,6,6],
                    [7,7,7,8,8,8,9,9,9],
                    [7,7,7,8,8,8,9,9,9],
                    [7,7,7,8,8,8,9,9,9],
                   ]
            return boxs[cell_index]

def col_of_cell_index(cell_index):
            global cell_containers
            col = cell_containers[cell_index].data["cell_col"]
            return col

def box_of(row, col):
            if row in range (1,4):
                if col in range (1,4): return 1
                if col in range (4,7): return 2
                return 3
            if row in range (4,7):
                if col in range (1,4): return 4
                if col in range (4,7): return 5
                return 6
            if col in range (1,4): return 7
            if col in range (4,7): return 8
            return 9

if __name__ == '__main__':
    print ('command line test of sudoke_util')
    assert  box_of(1,1)  == 1, ' box_of error' 
    assert  box_of(4,1)  == 4, ' box_of error' 
    assert  box_of(7,1)  == 7, ' box_of error' 
    #assert  box_of(7,1)  == 9, ' box_of error' 
    pass