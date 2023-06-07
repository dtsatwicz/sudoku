
import flet as ft

cell_containers=[]
import sudoku_util as su
import sudoku_x2 as x2

if __name__ == "__main__":

    text_action_to_take = 'No Action Set'
    next_cell_value = "__"

    def main(page: ft.Page):

        page.title="Sudoku"
        page.window_height=500
        page.window_width=360
        text_action_to_take = 'No Action Set'

        result = ft.Text(value='0')
        new_cell_value = ft.Text(value='0')
        text_action_to_take = 'No Action Set'
        action_to_take = ft.Text(value=text_action_to_take)
        next_cell_value = '0'
        new_value = ''

        def values_in_cells(cells,cell_containers):
            values = []
            for cell in cells:
                cell_current_value = cell_containers[cell].data["current_value"]
                if cell_current_value != "__":
                    values.append(cell_current_value)
            return values

    
        def cell_clicked(e):
            global cell_containers
            global next_cell_value
            global new_value
            global text_action_to_take

            print ('cell_clicked', text_action_to_take)
            print ('cell_clicked start', e.control.data)

            if text_action_to_take == 'No Action Set':
                print ('No Action Set')
            
            elif text_action_to_take == 'Set Cell To':
                e.control.content = ft.Text(next_cell_value)
                e.control.data["current_value"] = next_cell_value
                e.control.data["value_source"] = 'Set Cell To'
                e.control.bgcolor="red"
                page.update()
            
            elif text_action_to_take == 'Run Row Can Be':
                row = e.control.data["row"]
                cells_set = row_can_be(row,cell_containers)
                page.update()
            
            elif text_action_to_take == 'Run Col Can Be':
                col = e.control.data["col"]
                cells_set = col_can_be(col,cell_containers)
                page.update()
            
            elif text_action_to_take == 'Run Box Can Be':
                box = e.control.data["box"]
                cells_set = box_can_be(box,cell_containers)
                page.update()
            
            elif text_action_to_take == 'Run Cell Can Be':
                cell = e.control.data["index"]
                cells_set = cell_can_be(cell,cell_containers)
                page.update()
            
            elif text_action_to_take == 'Run All 4 Be':
                all4()
                page.update()
            
            else:
                print (text_action_to_take, ' is not implimented', )
            
            print ('cell_clicked end  ', e.control.data)

        def value_clicked(e):
            global next_cell_value
            global text_action_to_take
            global new_value

            print ('value_clicked', e.control.data)

            text_action_to_take = "Set Cell To"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            page.update()

            new_value = e.control.data["sudoku_value"]

            new_cell_value.current.controls.clear()
            new_cell_value.current.controls.append(ft.Text(new_value))
            next_cell_value = new_value
            page.update()

        def click_row_can_be(e):
            global text_action_to_take
            print ('click_row_can_be')
            text_action_to_take = "Run Row Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def click_col_can_be(e):
            global text_action_to_take
            print ('click_col_can_be')
            text_action_to_take = "Run Col Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def click_box_can_be(e):
            global text_action_to_take
            print ('click_box_can_be')
            text_action_to_take = "Run Box Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def click_cell_can_be(e):
            global text_action_to_take
            print ('click_cell_can_be')
            text_action_to_take = "Run Cell Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            page.update()

        def click_all_row_can_be(e):
            global cell_containers 
            global text_action_to_take
            print ('click_all_row_can_be')
            text_action_to_take = "Run All Row Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            page.update()
            all_row_can_be(cell_containers)
            
        def all_row_can_be(cell_containers):
            print ('all_row_can_be')
            for row in range (1 , 10):
                row_can_be(row,cell_containers)
            
        def click_all_col_can_be(e):
            global text_action_to_take
            print ('click_all_col_can_be')
            text_action_to_take = "Run All Col Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            page.update()
            all_col_can_be(cell_containers)
            
            
        def all_col_can_be(cell_containers):
            global text_action_to_take
            print ('all_col_can_be')
            for col in range (1 , 10):
                col_can_be(col,cell_containers)
            
        def click_all_box_can_be(e):
            global cell_containers
            global text_action_to_take
            print ('click_all_box_can_be')
            text_action_to_take = "Run All box Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            page.update()
            all_box_can_be(cell_containers)
            
        def all_box_can_be(cell_containers):
            print ('all_box_can_be')
            for box in range (1 , 10):
                box_can_be(box,cell_containers)


        def click_all_cell_can_be(e):
            global cell_containers
            global text_action_to_take
            print ('click_all_cell_can_be')
            text_action_to_take = "Run All Cell Can Be"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            page.update()
            all_cell_can_be(cell_containers)

        def all_cell_can_be(cell_containers):
            print ('all_cell_can_be')
            for cell in range (0 , 81):
                cell_can_be(cell,cell_containers)

        def click_all4(e):
            global cell_containers 
            global text_action_to_take
            print ('click_all4')
            text_action_to_take = "Run All 4"
            action_to_take.current.controls.clear()
            action_to_take.current.controls.append(ft.Text(text_action_to_take))
            #new_cell_value.current.controls.clear()
            all4(cell_containers)
            page.update()

        def all4(cell_containers):
            global next_cell_value
            next_cell_value = ""
            page.update()
            all_row_can_be(cell_containers)
            page.update()
            all_col_can_be(cell_containers)
            page.update()
            all_box_can_be(cell_containers)
            page.update()
            all_cell_can_be(cell_containers)
            page.update()

        def row_can_be(row,cell_containers):

            cells_set = []
            print (' 1 row_can_be', row)

            row_needs = su.sudoku_values()
            row_cells = su.cells_in_row(row)
            for row_cell in row_cells:
                cell_current_value = cell_containers[row_cell].data["current_value"]
                if cell_current_value != "__":
                    row_needs.remove (cell_current_value)
            print (' 2 row_can_be', row, 'row_needs ', row_needs)
             
            for needs in row_needs:
                print ('3a row_can_be row, needs ==>', row, needs)

                can_be_count = 0
                can_be_cell = -1
                can_be_col = -1
                cannot_reason = ''

                for col_cell in su.cells_in_row(row):
                    if can_be_count <= 1:
                        cell_current_value = cell_containers[col_cell].data["current_value"]
                        col = cell_containers[col_cell].data["col"]
            
                        print ('3b row_can_be row, col ', row, col, needs, can_be_count,  cell_current_value)

                        if cell_current_value == "__":
                            print ('3c row_can_be row, col ', 
                                   row, col, needs, can_be_count,  cell_current_value)

                            col_cells = su.cells_in_col(col)
                            col_values = values_in_cells(col_cells,cell_containers)
                            cannot_reason = ''
                            if needs in col_values:
                                can_be = False
                                cannot_reason = 'col cannot put value ' + needs + ' in col ' \
                                                  + str(col)
                                print ('5a row_can_be', row, col, needs, can_be_count, cannot_reason)
                            else:
                                box =  su.box_of(row, col)
                                box_cells = su.cells_in_box(box)
                                box_values = values_in_cells(box_cells,cell_containers)

                                if needs in box_values:
                                    can_be = False
                                    cannot_reason = 'box cannot put value ' + needs + ' in box ' \
                                                      + str(box)
                                    print ('5b row_can_be', row, col, needs, can_be_count, cannot_reason)
                                else:
                                    ## needs can go in this col_cell
                                    can_be_count += 1
                                    can_be_cell = col_cell
                                    can_be_col = col
                                    print (' 4 row_can_be row, col needs ==> cellCanBe', 
                                           row, col, needs, ' of row_needs', row_needs, col_cell)

                if can_be_count == 1:
                    cells_set.append([row, can_be_col, needs, can_be_cell])
                    cell_containers[can_be_cell].content = ft.Text(needs)
                    cell_containers[can_be_cell].data["current_value"] = needs
                    cell_containers[can_be_cell].data["value_source"] = 'row_can_be'
                    cell_containers[can_be_cell].content.bgcolor="orange"
                    page.update()
                    print ('6a row_can_be ==>', row, col, needs, can_be_count)
                    print ()
                else:
                    cannot_reason = 'cannot put value ' + needs + ' in col ' \
                    + str(col) + ' box ' + ' can_be_count= ' + str(can_be_count)
                    print ('6b row_can_be ', row, col, needs, cannot_reason)

                print (' 9 end of needs loop ', row, can_be_col, needs, can_be_count, 
                                               can_be_cell, cannot_reason)
                print ()

            print ('row_can_be returning', cells_set)
            pass
            return cells_set

        def col_can_be(col,cell_containers):
            ##global cell_containers

            cells_set = []

            ##col = data["col"]
            print (' 1 col_can_be', col)

            col_needs = su.sudoku_values()
            col_cells = su.cells_in_col(col)
            for col_cell in col_cells:
                cell_current_value = cell_containers[col_cell].data["current_value"]
                if cell_current_value != "__":
                    col_needs.remove (cell_current_value)
            print (' 2 col_can_be', col, 'col_needs ', col_needs)
             
            for needs in col_needs:
                print ('3a col_can_be col, needs ==>', col, needs)

                can_be_count = 0
                can_be_cell = -1
                can_be_row = -1
                cannot_reason = ''

                for row_cell in su.cells_in_col(col):
                    if can_be_count <= 1:
                        cell_current_value = cell_containers[row_cell].data["current_value"]
                        row = cell_containers[row_cell].data["row"]
            
                        print ('3b col_can_be row, col ', row, col, needs, can_be_count,  cell_current_value)

                        if cell_current_value == "__":
                            print ('3c col_can_be row, col ', 
                                   row, col, needs, can_be_count,  cell_current_value)

                            row_cells = su.cells_in_row(row)
                            row_values = values_in_cells(row_cells,cell_containers)
                            cannot_reason = ''
                            if needs in row_values:
                                can_be = False
                                cannot_reason = 'row cannot put value ' + needs + ' in row ' \
                                                  + str(row)
                                print ('5a col_can_be', row, col, needs, can_be_count, cannot_reason)
                            else:
                                box =  su.box_of(row, col)
                                box_cells = su.cells_in_box(box)
                                box_values = values_in_cells(box_cells,cell_containers)

                                if needs in box_values:
                                    can_be = False
                                    cannot_reason = 'box cannot put value ' + needs + ' in box ' \
                                                      + str(box)
                                    print ('5b col_can_be', row, col, needs, can_be_count, cannot_reason)
                                else:
                                    ## needs can go in this row_cell
                                    can_be_count += 1
                                    can_be_cell = row_cell
                                    can_be_row = row
                                    print (' 4 col_can_be row, col needs ==> cellCanBe', 
                                           row, col, needs, ' of col_needs', col_needs, row_cell)

                if can_be_count == 1:
                    cells_set.append([col, can_be_row, needs, can_be_cell])
                    cell_containers[can_be_cell].content = ft.Text(needs)
                    cell_containers[can_be_cell].data["current_value"] = needs
                    cell_containers[can_be_cell].data["value_source"] = 'col_can_be'
                    cell_containers[can_be_cell].content.bgcolor="orange"
                    page.update()
                    print ('6a col_can_be ==>', row, col, needs, can_be_count)
                    print ()
                else:
                    cannot_reason = 'cannot put value ' + needs + ' in row ' \
                    + str(row) + ' box ' + ' can_be_count= ' + str(can_be_count)
                    print ('6b row_can_be ', row, col, needs, cannot_reason)

                print (' 9 end of needs loop ', row, can_be_row, needs, can_be_count, 
                                               can_be_cell, cannot_reason)
                print ()

            print ('col_can_be returning', cells_set)
            pass
            return cells_set

        def box_can_be(box,cell_containers):

            cells_set = []

            ##box = data["cell_box"]
            print (' 1 box_can_be', box)

            box_needs = su.sudoku_values()
            box_cells = su.cells_in_box(box)
            for box_cell in box_cells:
                cell_current_value = cell_containers[box_cell].data["current_value"]
                if cell_current_value != "__":
                    box_needs.remove (cell_current_value)
            print (' 2 box_can_be', box, 'box_needs ', box_needs)
             
            for needs in box_needs:
                print ('3a box_can_be box, needs ==>', box, needs)

                can_be_count = 0
                can_be_cell = -1
                can_be_row = -1
                can_be_col = -1
                cannot_reason = ''

                for box_cell in su.cells_in_box(box):

                    row = cell_containers[box_cell].data["row"]
                    row_cells = su.cells_in_row(row)
                    row_values = values_in_cells(row_cells,cell_containers)

                    col = cell_containers[box_cell].data["col"]
                    col_cells = su.cells_in_col(col)
                    col_values = values_in_cells(col_cells,cell_containers)

                    if can_be_count <= 1:
                        cell_current_value = cell_containers[box_cell].data["current_value"]
            
                        print ('3b box_can_be box, row, col ', box, row, needs, can_be_count,  cell_current_value)

                        if cell_current_value == "__":
                            print ('3c box_can_be box, row, col ', 
                                   box, row, col, needs, can_be_count,  cell_current_value)

                            col_cells = su.cells_in_col(col)
                            col_values = values_in_cells(col_cells,cell_containers)
                            cannot_reason = ''
                            if needs in col_values or needs in row_values:
                                can_be = False
                                cannot_reason = 'box cannot put value ' + needs \
                                    + 'in row ' + str(row) + ' in col ' + str(col)
                                print ('5a box_can_be', box, row, col, needs, can_be_count, cannot_reason)
                            else:
                                ## needs can go in this col_cell
                                can_be_count += 1
                                can_be_cell = box_cell
                                can_be_row = row
                                can_be_col = col
                                print (' 4 box_can_be row, col needs ==> cellCanBe', 
                                        row, col, needs, ' of box_needs', box_needs, box_cell)

                if can_be_count == 1:
                    cells_set.append([row, can_be_col, needs, can_be_cell])
                    cell_containers[can_be_cell].content = ft.Text(needs)
                    cell_containers[can_be_cell].data["current_value"] = needs
                    cell_containers[can_be_cell].data["value_source"] = 'box_can_be'
                    cell_containers[can_be_cell].content.bgcolor="orange"
                    page.update()
                    print ('6a box_can_be ==>', row, col, needs, can_be_count)
                    print ()
                else:
                    cannot_reason = 'cannot put value ' + needs + ' in col ' \
                    + str(col) + ' row ' + ' can_be_count= ' + str(can_be_count)
                    print ('6b box_can_be ', row, col, needs, cannot_reason)

                print (' 9 end of needs loop ', row, can_be_col, needs, can_be_count, 
                                               can_be_cell, cannot_reason)
                print ()

            print ('box_can_be returning', cells_set)
            pass
            return cells_set

        def cell_can_be(cell,cell_containers):
            row = cell_containers[cell].data["row"]
            col = cell_containers[cell].data["col"]
            box = cell_containers[cell].data["box"]
            value = cell_containers[cell].data["current_value"]
            print ('cell_can_be', row, col, box, cell, value)

            cells_set=[]
            cell_can_be_values=[]
            if value in su.sudoku_values():
                return cells_set, cell_can_be_values

            cell_can_be_values = su.sudoku_values()
            row_values = values_in_cells(su.cells_in_row(row),cell_containers)
            for try_value in row_values:
                if try_value in values_in_cells(su.cells_in_row(row),cell_containers):
                    if try_value in cell_can_be_values:
                        cell_can_be_values.remove(try_value)
            col_values = values_in_cells(su.cells_in_col(col),cell_containers)
            for try_value in col_values:
                if try_value in values_in_cells(su.cells_in_col(col),cell_containers):
                    if try_value in cell_can_be_values:
                        cell_can_be_values.remove(try_value)
            box_values = values_in_cells(su.cells_in_box(box),cell_containers)
            for try_value in box_values:
                if try_value in values_in_cells(su.cells_in_box(box),cell_containers):
                    if try_value in cell_can_be_values:
                        cell_can_be_values.remove(try_value)
            print("cell_can_be", cell_can_be_values)

            if len(cell_can_be_values) == 1:
                cells_set.append([row, col, cell_can_be_values[0], cell])
                cell_containers[cell].content = ft.Text(cell_can_be_values[0])
                cell_containers[cell].data["current_value"] = cell_can_be_values[0]
                cell_containers[cell].data["value_source"] = 'cell_can_be'
                cell_containers[cell].data["show_can_be"] = ''
                cell_containers[cell].content.bgcolor="blue"
                page.update()
                print ('cell_can_be ==>', row, col, cell_can_be_values)
                print ()
                pass
            elif len(cell_can_be_values) > 1:
                show_can_be = ''.join(cell_can_be_values)
                cell_containers[cell].content = ft.Text(show_can_be)
                cell_containers[cell].data["current_value"] = "__"
                cell_containers[cell].data["value_source"] = 'cell_can_be'
                cell_containers[cell].data["show_can_be"] = show_can_be
                cell_containers[cell].content.bgcolor="red"
                page.update()
                print ('cell_can_be ==>', row, col, cell_can_be_values)
                print ()
                pass
            pass

        def click_setup(e):
            global cell_containers
            global next_cell_value
            next_cell_value = "3"
            click_init(e)
            all_row_can_be(cell_containers)
            all_col_can_be(cell_containers)
            all_box_can_be(cell_containers)

            all_row_can_be(cell_containers)
            all_col_can_be(cell_containers)
            all_box_can_be(cell_containers)

            all_cell_can_be(cell_containers)

        def click_init(e):
            global cell_containers
            global next_cell_value
            global try_new_value
            
            if next_cell_value == "1": ## solves with all4 6 times
                init_values = '...65....' + '.96..14..' + '...9..3.1' \
                            + '..5..7.9.' + '.1......6' + '2..1...3.' \
                            + '5..71.6..' + '.....45..' + '.8.2.....'
            elif next_cell_value == "2": ## maybe damaged -- does not get far
                init_values = '81.4...5.' + '......9..' + '92.7...18' \
                            + '5..9.....' + '.92...57.' + '.....4..6' \
                            + '26...8.45' + '..7......' + '.8...5.63'
            elif next_cell_value == "3": ## col 9 167+167+67 > elim 167 9,9 = 2
                init_values = '..43...9.' + '...6..1..' + '......7..' \
                            + '..8.6....' + '1.....6.8' + '.238.....' \
                            + '.9...6.2.' + '.852.3.1.' + '...4....5'
            elif next_cell_value == "4":
                init_values = '.73..9...' + '.4..1....' + '9..5....8' \
                            + '...4...2.' + '....3..5.' + '7.625....' \
                            + '6...8..9.' + '..4..21..' + '...9..34.'
            else:
                init_values = '.........' + '.........' + '.........' \
                            + '.........' + '.........' + '.........' \
                            + '.........' + '.........' + '.........'


            print ("click_init" )

            for cell_index in range (81):

                text_new_value = init_values[cell_index]
                if text_new_value == '.': text_new_value = '__'

                cell_containers[cell_index].content = ft.Text(text_new_value)
                cell_containers[cell_index].data["current_value"] = text_new_value
                cell_containers[cell_index].data["value_source"] = 'init'
                cell_containers[cell_index].bgcolor="green"

                page.update()

        def sudoku_grid():
            global cell_containers

            cell_containers=[]
            cell_index = 0
            for row in range (1,10):
                this_row = []
                this_row.append( ft.VerticalDivider(width=3,thickness=3, color="black"))
                for col in range (1,10):
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
                    this_row.append(c)
                    if col in (3,6,9):
                        this_row.append( ft.VerticalDivider(width=3,thickness=3, color="black"))

                if row == 1 :
                    page.add(ft.Divider(height=3,thickness=3,color='black'))
                page.add(ft.Row(this_row,spacing=1,height=50,expand=True))
                if row in (3,6,9):
                    page.add(ft.Divider(height=3,thickness=3,color='black'))

            this_row = []
            this_row.append(ft.Row(controls=[action_to_take],ref=action_to_take,data=ft.Text('No Action Set')))
            this_row.append(ft.Row(controls=[new_cell_value],ref=new_cell_value,data=ft.Text('__')))
            page.add(ft.Row(this_row,spacing=1,expand=True))
            next_cell_value = '0'

            set_values = []        

            for value in su.sudoku_values() + ['__']:
                c = ft.Container(
    				    content=ft.Text(value),
    			    	width=18,
    				    height=20,
    				    bgcolor="green",
    				    ink=False,
					    data= {
    					   "sudoku_value": value,
                           "bgcolor": "green",
                            },
    				    on_click=value_clicked,
    				)

                set_values.append(c)

            page.add(ft.Row(set_values))
            next_cell_value = '__'

            commands = []
            c = ft.Container(
	        		content=ft.Text('Row'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
	        		on_click=click_row_can_be,
                    )
            commands.append(c)        
            c = ft.Container(
	        		content=ft.Text('Col'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
                    on_click=click_col_can_be,
                    )
            commands.append(c)        
            c = ft.Container(
	        		content=ft.Text('Box'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
	        		on_click=click_box_can_be,
                    )
            commands.append(c)        
            c = ft.Container(
	        		content=ft.Text('Cell'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
                    on_click=click_cell_can_be,
                    )
            commands.append(c)        

            page.add(ft.Row(commands,spacing=1,expand=True))
            commands = []
            c = ft.Container(
	        		content=ft.Text('AllRow'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
	        		on_click=click_all_row_can_be,
                    )
            commands.append(c)        
            c = ft.Container(
	        		content=ft.Text('AllCol'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
                    on_click=click_all_col_can_be,
                    )
            commands.append(c)        
            c = ft.Container(
	        		content=ft.Text('AllBox'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
	        		on_click=click_all_box_can_be,
                    )
            commands.append(c)        
            c = ft.Container(
	        		content=ft.Text('AllCell'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
                    on_click=click_all_cell_can_be,
                    )
            commands.append(c)        
            c = ft.Container(
	        		content=ft.Text('All4'),
                    width = 55,
                    height = 30,
    				bgcolor="green",
    				ink=False,
                    on_click=click_all4,
                    )
            commands.append(c)        

            page.add(ft.Row(commands,spacing=1,expand=True))

            page.add(
	        	ft.Row(
	        		controls=[
	        			ft.ElevatedButton(text='Init',on_click=click_init),
	        			ft.ElevatedButton(text='Setup',on_click=click_setup),
	            		]
	                ),
                )    

        sudoku_grid()

    ft.app(target=main)
    ##ft.app(target=main,view=ft.WEB_BROWSER)