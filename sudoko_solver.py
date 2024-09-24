#define the checker function
#checks whether a number can be placed in that cell following the rules of SUDOKO
def is_valid(grid,row,col,number): 
    for x in range(9): 
        if grid[row]==number:
            return False
    
    for x in range(9):
        if grid[col]==number:
            return False
        
    corner_row= row-row%3
    corner_col=col-col%3
    for x in range(3):
        for y in range(3):
            if grid[corner_row+x][corner_col+y]==number:
                return False
            
    return True 
#define the solving function, checked by placing all the numbers recursively 
def solve(grid,row,col): 
    if col==9:
        if row==8:
            return True
        row+=1
        col=0

    if grid[row][col]>0:
        return solve(grid,row,col+1)#recursion
    
    for num in range(1,10):
        if is_valid(grid,row,col,num):
            grid[row][col]=num #if the number is valid then the number is placed in that cell

            if solve(grid,row,col+1):
                return True
            
    grid[row][col]=0 

    return False
print("enter the grid to be solved")
grid=[]
for i in range(num):
    row_elements=list(map(int,input("enter the rows of the sudoko").split()))
    grid.append(row_elements)

if solve(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()

else:
    print("no solution")
