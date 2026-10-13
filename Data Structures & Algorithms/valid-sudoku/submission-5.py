class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #We check every row
        for row in board:
            row_entry_seen = set()
            #Check whether we have seen the number before
            for num in row:
                if num != ".":
                    if num in row_entry_seen:
                        #If we have seen the number before we return False
                        return False
                    else:
                        #If we have not seen it yet we add it to the set
                        row_entry_seen.add(num)
                else:
                    continue
            #If the loop runs without returning then that row is fine and we can move onto the next
            continue
        #We make a list containing all the columns
        columns = []
        for i in range(9):
            column_list = []
            for row in board:
                column_list.append(row[i])
            columns.append(column_list)
        #Do the exact same thing as before but for the columns

        for col in columns:
            col_entry_seen = set()
            #Check whether we have seen the number before
            for num in col:
                if num != ".":
                    if num in col_entry_seen:
                        #If we have seen the number before we return False
                        return False
                    else:
                        #If we have not seen it yet we add it to the set
                        col_entry_seen.add(num)
                else:
                    continue
            #If the loop runs without returning then that row is fine and we can move onto the next
            continue
        
        sub_grids = []
        index_list = [0,3,6]
        for i in index_list:
            for j in index_list:
                sub_grids.append(board[j][i:i+3]+board[j+1][i:i+3]+board[j+2][i:i+3])

        for grid in sub_grids:
            sub_grid_entry_seen = set()
            #Check whether we have seen the number before
            for num in grid:
                if num != ".":
                    if num in sub_grid_entry_seen:
                        #If we have seen the number before we return False
                        return False
                    else:
                        #If we have not seen it yet we add it to the set
                        sub_grid_entry_seen.add(num)
                else:
                    continue
            #If the loop runs without returning then that row is fine and we can move onto the next
            continue
        
        return True
        



        

        

                


        