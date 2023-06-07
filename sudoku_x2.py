# sudoku_x2.py

import sudoku_util as su

def x2_in_cells(cell_containers):
            show_can_be_values = []
            for row in (1,10):
                for cell in su.cells_in_row(row):
                    if cell_containers(cell).data["current_value"] == '__':
                        show_can_be_values.append(cell_containers(cell).data["show_can_be"])
                len = len(show_can_be_values)
                if len(show_can_be_values) >= 3:
                    show_index = 0
                    for show_value in show_can_be_values:
                        for check_value in show_can_be_values[show_index:]:
                            print ('found', check_value, show_index)
                            show_index += 1
                             
                                
if __name__ == "__main__":

    import flet as ft    
    cell_containers=[]
    for cell in range(81):


						data= {"index": cell_index,
								"row": row,
								"col": col,
								"box": box,
								"current_value": '__',
                                "bgcolor": "blue",
                                "highlighted": False,
								"value_source": ''},


        c = ft.Container{
             data= {"current_value": '__',
                    
        row = su.row_of_cell(cell)
        col = su.col_of_cell(cell)
        box = su.box_of(row,col)
                    c = ft.Container(
						content=ft.Text("__"),
						width=35,
						height=50,
						bgcolor="blue",
						ink=False,
						data= {"index": cell_index,
								"row": row,
								"col": col,
								"box": box,
								"current_value": '__',
                                "bgcolor": "blue",
                                "highlighted": False,
								"value_source": ''},
						on_click=cell_clicked,
						)

                    cell_index += 1

                    cell_containers.append(c)