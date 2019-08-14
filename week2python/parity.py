## TASK 1
# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user
# coordinate = [] 

# coordinate= input('Input your location in format (row,col)')

# print(coordinate)
# rowlocation = coordinate[0]
# collocation = coordinate[1]

# if five_by_five_grid[row][col] == 0:
#     five_by_five_grid[row][col] = x
# else
#     five_by_five_grid[row][col] = o

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','X'],
    ['X','0','X','0','X'],
    ['0','0','0','X','X'],
    ['X','0','0','X','X']
]



for row in range(0,5):
    rowcountx = 0
    for col in range(0,5):
        print(five_by_five_grid[row][col],',', end=' ')
        if five_by_five_grid[row][col] == 'X':
            rowcountx = rowcountx + 1 
    if rowcountx%2 == 0:
        five_by_five_grid.insert((row,6),'0')
    else:
        five_by_five_grid.insert((row,6),'X')

    print('\n')   

# first step is to add colum 6 and row 6
# output the grid to the user
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)
# output the grid with the flipped card

## TASK 2

# given a six by six grid, work out what card was flipped
# ​
# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)