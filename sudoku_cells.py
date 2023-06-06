# sudoku_cells.py

def values_in_cells(cells,cell_containers):
            values = []
            for cell in cells:
                cell_current_value = cell_containers[cell].data["cell_current_value"]
                if cell_current_value != "__":
                    values.append(cell_current_value)
            return values
